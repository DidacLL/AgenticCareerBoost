from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path


def resolve_script() -> Path:
    env_path = os.environ.get("FILL_COVER_LETTER_SCRIPT")
    if env_path:
        return Path(env_path).resolve()

    same_folder = Path(__file__).with_name("fill_cover_letter.py").resolve()
    if same_folder.exists():
        return same_folder

    parent_scripts = Path(__file__).resolve().parent / "scripts" / "fill_cover_letter.py"
    if parent_scripts.exists():
        return parent_scripts.resolve()

    return same_folder


SCRIPT = resolve_script()


def run_cli(tmp_path: Path, *args: str) -> subprocess.CompletedProcess[str]:
    assert SCRIPT.exists(), (
        f"Script not found: {SCRIPT}\n"
        "Put fill_cover_letter.py next to test_fill_cover_letter.py, "
        "or run with FILL_COVER_LETTER_SCRIPT=/path/to/fill_cover_letter.py pytest."
    )

    return subprocess.run(
        [sys.executable, str(SCRIPT), *map(str, args)],
        cwd=tmp_path,
        text=True,
        capture_output=True,
    )

def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_list_detects_unique_sorted_keys(tmp_path: Path) -> None:
    template = write(
        tmp_path / "template.tex",
        "A ::ROLE:: B ::TO:: C ::ROLE:: D ::LLM-STRENGTHS::",
    )

    result = run_cli(tmp_path, template, "--list")

    assert result.returncode == 0
    assert result.stdout.splitlines() == ["LLM-STRENGTHS", "ROLE", "TO"]


def test_init_values_creates_json_skeleton(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: ::ROLE:: ::LOCATION::")
    values = tmp_path / "values.json"

    result = run_cli(tmp_path, template, "--init-values", values)

    assert result.returncode == 0
    assert json.loads(read(values)) == {
        "LOCATION": "",
        "ROLE": "",
        "TO": "",
    }


def test_generates_letter_from_json_values(tmp_path: Path) -> None:
    template = write(
        tmp_path / "template.tex",
        "Dear ::TO::,\nApplication for ::ROLE:: in ::LOCATION::.\n::CONTENT::",
    )
    values = write(
        tmp_path / "values.json",
        json.dumps(
            {
                "TO": "Acme Robotics",
                "ROLE": "Platform Engineer",
                "LOCATION": "Barcelona",
                "CONTENT": "I build reliable internal tools.",
            }
        ),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == (
        "Dear Acme Robotics,\n"
        "Application for Platform Engineer in Barcelona.\n"
        "I build reliable internal tools."
    )


def test_set_argument_overrides_json_value(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: ::ROLE::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "OldCo", "ROLE": "Engineer"}))
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--values",
        values,
        "--set",
        "TO=NewCo",
        "--output",
        output,
    )

    assert result.returncode == 0
    assert read(output) == "NewCo Engineer"


def test_set_can_read_long_value_from_file(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "Body:\n::CONTENT::")
    body = write(tmp_path / "body.txt", "Paragraph one.\n\nParagraph two.")
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--set",
        f"CONTENT@={body}",
        "--output",
        output,
    )

    assert result.returncode == 0
    assert read(output) == "Body:\nParagraph one.\n\nParagraph two."


def test_extra_values_are_ignored_and_reported_to_stderr(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "Acme", "UNUSED": "x"}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == "Acme"
    assert "Ignored extra values: UNUSED" in result.stderr


def test_missing_value_fails_by_default(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: ::ROLE::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "Acme"}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode != 0
    assert "Missing values: ROLE" in result.stderr
    assert not output.exists()


def test_allow_missing_keeps_unresolved_placeholder(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: ::ROLE::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "Acme"}))
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--values",
        values,
        "--output",
        output,
        "--allow-missing",
    )

    assert result.returncode == 0
    assert read(output) == "Acme ::ROLE::"


def test_unresolved_placeholder_introduced_by_value_fails(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::")
    values = write(tmp_path / "values.json", json.dumps({"CONTENT": "Nested ::TO::"}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode != 0
    assert "Unresolved placeholders: TO" in result.stderr


def test_escape_latex_special_characters(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::")
    values = write(
        tmp_path / "values.json",
        json.dumps({"CONTENT": r"A&B 50% $x #1 _id {ok} ~ ^ \ end"}),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output, "--escape")

    assert result.returncode == 0
    assert read(output) == (
        r"A\&B 50\% \$x \#1 \_id \{ok\} "
        r"\textasciitilde{} \textasciicircum{} \textbackslash{} end"
    )


def test_raw_key_is_not_escaped_when_escape_is_enabled(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::\n::TO::")
    values = write(
        tmp_path / "values.json",
        json.dumps(
            {
                "CONTENT": r"\textbf{Already LaTeX-ready & intentional}",
                "TO": "R&D Team",
            }
        ),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--values",
        values,
        "--output",
        output,
        "--escape",
        "--raw-key",
        "CONTENT",
    )

    assert result.returncode == 0
    assert read(output) == (
        r"\textbf{Already LaTeX-ready & intentional}" "\n"
        r"R\&D Team"
    )


def test_unicode_values_are_preserved(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: — ::LOCATION:: — ::CONTENT::")
    values = write(
        tmp_path / "values.json",
        json.dumps(
            {
                "TO": "Equip d’enginyeria",
                "LOCATION": "Barcelona / remoto",
                "CONTENT": "Python, documentación técnica y sistemas agenticos.",
            },
            ensure_ascii=False,
        ),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == (
        "Equip d’enginyeria — Barcelona / remoto — "
        "Python, documentación técnica y sistemas agenticos."
    )


def test_empty_string_value_is_valid(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "A::OPTIONAL::B")
    values = write(tmp_path / "values.json", json.dumps({"OPTIONAL": ""}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == "AB"


def test_none_and_non_string_json_values_are_converted(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::A:: ::B:: ::C::")
    values = write(tmp_path / "values.json", json.dumps({"A": None, "B": 123, "C": True}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == " 123 True"


def test_nested_output_directory_is_created(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "Acme"}))
    output = tmp_path / "generated" / "letters" / "acme.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == "Acme"


def test_invalid_json_fails(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")
    values = write(tmp_path / "values.json", "{not valid json")
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode != 0
    assert "Invalid JSON" in result.stderr


def test_json_array_fails(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")
    values = write(tmp_path / "values.json", json.dumps(["not", "an", "object"]))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode != 0
    assert "Values file must contain a JSON object" in result.stderr


def test_missing_template_fails(tmp_path: Path) -> None:
    result = run_cli(tmp_path, tmp_path / "missing.tex", "--list")

    assert result.returncode != 0
    assert "Missing file:" in result.stderr


def test_output_is_required_for_generation(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")

    result = run_cli(tmp_path, template, "--set", "TO=Acme")

    assert result.returncode != 0
    assert "--output is required" in result.stderr


def test_invalid_set_argument_fails(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO::")
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--set", "TO", "--output", output)

    assert result.returncode != 0
    assert "Invalid --set value" in result.stderr


def test_set_file_missing_fails(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::")
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--set",
        f"CONTENT@={tmp_path / 'missing.txt'}",
        "--output",
        output,
    )

    assert result.returncode != 0
    assert "Missing file:" in result.stderr


def test_invalid_placeholder_shapes_are_ignored(tmp_path: Path) -> None:
    template = write(
        tmp_path / "template.tex",
        "::VALID:: ::-INVALID:: :::: ::SPACE KEY:: ::A.B::",
    )

    result = run_cli(tmp_path, template, "--list")

    assert result.returncode == 0
    assert result.stdout.splitlines() == ["VALID"]


def test_large_number_of_placeholders(tmp_path: Path) -> None:
    count = 500
    keys = [f"KEY-{i}" for i in range(count)]
    template = write(tmp_path / "template.tex", "\n".join(f"::{key}::" for key in keys))
    values = write(
        tmp_path / "values.json",
        json.dumps({key: f"value-{i}" for i, key in enumerate(keys)}),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    lines = read(output).splitlines()
    assert len(lines) == count
    assert lines[0] == "value-0"
    assert lines[-1] == f"value-{count - 1}"


def test_large_multiline_content_value(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::")
    large_body = "\n".join(f"Paragraph line {i}: fake evidence." for i in range(2000))
    body_file = write(tmp_path / "body.txt", large_body)
    output = tmp_path / "letter.tex"

    result = run_cli(
        tmp_path,
        template,
        "--set",
        f"CONTENT@={body_file}",
        "--output",
        output,
    )

    assert result.returncode == 0
    assert read(output) == large_body


def test_many_placeholder_like_sequences_inside_normal_text(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::CONTENT::")
    values = write(
        tmp_path / "values.json",
        json.dumps({"CONTENT": " ".join([":not-a-key:", "::not valid::", "plain"] * 500)}),
    )
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert "plain" in read(output)


def test_repeated_placeholder_replaced_everywhere(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::TO:: ::TO:: ::TO::")
    values = write(tmp_path / "values.json", json.dumps({"TO": "Acme"}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == "Acme Acme Acme"


def test_case_sensitive_keys(tmp_path: Path) -> None:
    template = write(tmp_path / "template.tex", "::ROLE:: ::role::")
    values = write(tmp_path / "values.json", json.dumps({"ROLE": "Engineer", "role": "lower"}))
    output = tmp_path / "letter.tex"

    result = run_cli(tmp_path, template, "--values", values, "--output", output)

    assert result.returncode == 0
    assert read(output) == "Engineer lower"
