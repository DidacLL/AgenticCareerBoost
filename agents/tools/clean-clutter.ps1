<#
.SYNOPSIS
  Clean generated clutter from AgenticCareerBoost.

.DESCRIPTION
  Deletes only:
  - LaTeX auxiliary files by known extensions.
  - Explicit generated/cache folders.
  - Python cache folders named __pycache__.
  - Optional dependency/build folders with -Deep.

  Does NOT delete:
  - .tex source files
  - .pdf files
  - site/data/status.json
#>

param(
    [switch]$Apply,
    [switch]$Deep
)

$ErrorActionPreference = "Stop"

function Get-RepoRoot {
    try {
        $root = (& git rev-parse --show-toplevel 2>$null).Trim()
        if ($root) { return $root }
    } catch {
    }

    return (Get-Location).Path
}

$RepoRoot = Get-RepoRoot
Set-Location $RepoRoot

Write-Host "[clean-clutter] Repository: $RepoRoot"

if (-not $Apply) {
    Write-Host "[clean-clutter] Preview mode. Add -Apply to delete." -ForegroundColor Yellow
}

function Get-RelativePath {
    param([string]$Path)

    $resolved = Resolve-Path -LiteralPath $Path
    return $resolved.Path.Substring($RepoRoot.Length).TrimStart("\", "/")
}

function Remove-PathIfExists {
    param([string]$Path)

    if (-not (Test-Path -LiteralPath $Path)) {
        return
    }

    $relative = Get-RelativePath -Path $Path

    if ($Apply) {
        Remove-Item -LiteralPath $Path -Recurse -Force
        Write-Host "deleted: $relative" -ForegroundColor Green
    } else {
        Write-Host "would delete: $relative" -ForegroundColor DarkYellow
    }
}

function Remove-FilesByExtension {
    param([string[]]$Extensions)

    foreach ($ext in $Extensions) {
        Get-ChildItem -Path $RepoRoot -Recurse -Force -File -Filter "*$ext" -ErrorAction SilentlyContinue |
            Where-Object {
                $_.FullName -notmatch "\\\.git\\" -and
                $_.FullName -notmatch "\\node_modules\\" -and
                $_.FullName -notmatch "\\vendor\\"
            } |
            ForEach-Object {
                $relative = $_.FullName.Substring($RepoRoot.Length).TrimStart("\", "/")

                if ($Apply) {
                    Remove-Item -LiteralPath $_.FullName -Force
                    Write-Host "deleted: $relative" -ForegroundColor Green
                } else {
                    Write-Host "would delete: $relative" -ForegroundColor DarkYellow
                }
            }
    }
}

$LatexAuxExtensions = @(
    ".aux",
    ".bbl",
    ".bcf",
    ".blg",
    ".dvi",
    ".fdb_latexmk",
    ".fls",
    ".glg",
    ".glo",
    ".gls",
    ".idx",
    ".ilg",
    ".ind",
    ".ist",
    ".lof",
    ".log",
    ".lot",
    ".nav",
    ".out",
    ".run.xml",
    ".snm",
    ".synctex.gz",
    ".synctex(busy)",
    ".toc",
    ".vrb",
    ".xdv"
)

$GeneratedDirs = @(
    "agents/reports/tex/build",
    "agents/cv/build",
    "site/_site",
    "site/.jekyll-cache",
    "site/.sass-cache",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".tox",
    ".nox",
    "htmlcov",
    ".codex-tmp",
    ".agents"
)

$CacheDirNames = @(
    "__pycache__"
)

$DeepDirNames = @(
    "node_modules",
    "vendor",
    ".bundle",
    "dist",
    "build",
    ".next",
    ".parcel-cache",
    ".turbo",
    "coverage"
)

Write-Host "`n[clean-clutter] LaTeX auxiliary files"
Remove-FilesByExtension -Extensions $LatexAuxExtensions

Write-Host "`n[clean-clutter] Generated/cache folders"
foreach ($dir in $GeneratedDirs) {
    Remove-PathIfExists -Path (Join-Path $RepoRoot $dir)
}

Write-Host "`n[clean-clutter] Python cache folders"
foreach ($name in $CacheDirNames) {
    Get-ChildItem -Path $RepoRoot -Recurse -Force -Directory -Filter $name -ErrorAction SilentlyContinue |
        Where-Object { $_.FullName -notmatch "\\\.git\\" } |
        ForEach-Object { Remove-PathIfExists -Path $_.FullName }
}

if ($Deep) {
    Write-Host "`n[clean-clutter] Deep cleanup folders"

    foreach ($name in $DeepDirNames) {
        Get-ChildItem -Path $RepoRoot -Recurse -Force -Directory -Filter $name -ErrorAction SilentlyContinue |
            Where-Object { $_.FullName -notmatch "\\\.git\\" } |
            ForEach-Object { Remove-PathIfExists -Path $_.FullName }
    }
}

Write-Host "`n[clean-clutter] Done."

if (-not $Apply) {
    Write-Host "[clean-clutter] Nothing was deleted. Re-run with -Apply." -ForegroundColor Yellow
}
