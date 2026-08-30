param(
    [Parameter(Mandatory = $true)]
    [string]$Name
)

$tracker = $PSScriptRoot
$private = Join-Path $tracker ".private"
$generated = Join-Path $private "generated"

$json = Join-Path $private "$Name.json"
$letter = Get-Content -LiteralPath $json -Raw | ConvertFrom-Json
$texName = [System.IO.Path]::ChangeExtension($letter.output_pdf, ".tex")

if ([System.IO.Path]::GetFileName($texName) -ne $texName) {
    throw "output_pdf must be a plain filename"
}

$tex  = Join-Path $generated $texName
$pdf  = [System.IO.Path]::ChangeExtension($tex, ".pdf")

python "$tracker\render_letter.py" --input "$json" --output-dir "$generated"

if ($LASTEXITCODE -ne 0) {
    throw "render_letter.py failed"
}

for ($pass = 1; $pass -le 3; $pass++) {
    pdflatex `
        -interaction=nonstopmode `
        -halt-on-error `
        -output-directory "$generated" `
        "$tex"

    if ($LASTEXITCODE -ne 0) {
        throw "pdflatex failed on pass $pass"
    }
}

# Cleanup only if all 3 passes succeeded
$base = Join-Path $generated ([System.IO.Path]::GetFileNameWithoutExtension($tex))

$auxFiles = @(
    "$base.aux",
    "$base.log",
    "$base.out",
    "$base.toc",
    "$base.fls",
    "$base.fdb_latexmk",
    "$base.synctex.gz"
)

foreach ($file in $auxFiles) {
    if (Test-Path $file) {
        Remove-Item $file -Force
    }
}

Write-Host "Generated: $pdf"
Write-Host "Auxiliary files cleaned."
