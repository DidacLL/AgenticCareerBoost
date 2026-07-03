<#
.SYNOPSIS
    Build public CV and cover-letter PDFs from agents/cv/artifacts.json.
#>

$ErrorActionPreference = "Stop"
$cvRoot = $PSScriptRoot

function Test-LatexmkWorks {
    try {
        & latexmk --version *> $null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Invoke-CvTexBuild {
    param([string]$TexFile, [string]$Label)

    Write-Host "[cv-build] Building $Label..." -ForegroundColor Cyan
    if ($script:useLatexmk) {
        & latexmk -r latexmkrc -pdf -interaction=nonstopmode -halt-on-error $TexFile
        if ($LASTEXITCODE -ne 0) { throw "latexmk failed for $TexFile" }
        return
    }

    if (-not (Test-Path "build")) {
        New-Item -ItemType Directory -Path "build" -Force | Out-Null
    }
    $pdfArgs = @(
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory=build",
        "-aux-directory=build",
        $TexFile
    )
    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "  pass $pass/3..." -NoNewline -ForegroundColor DarkGray
        $proc = Start-Process -FilePath "pdflatex" -ArgumentList $pdfArgs -NoNewWindow -Wait -PassThru -RedirectStandardOutput "NUL" 2>&1
        if ($proc.ExitCode -ne 0) {
            Write-Host " FAILED" -ForegroundColor Red
            throw "pdflatex failed for $TexFile"
        }
        Write-Host " ok" -ForegroundColor DarkGray
    }
}

Push-Location $cvRoot
try {
    if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
        throw "python not found"
    }
    if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue) -and -not (Get-Command latexmk -ErrorAction SilentlyContinue)) {
        throw "pdflatex or latexmk not found. Install TeX Live or MiKTeX first."
    }

    $script:useLatexmk = Test-LatexmkWorks
    & python tools/artifact_manifest.py validate
    if ($LASTEXITCODE -ne 0) { throw "artifact manifest validation failed" }
    & python tools/render-cover-letter.py --all
    if ($LASTEXITCODE -ne 0) { throw "cover-letter rendering failed" }

    $roots = & python tools/artifact_manifest.py roots
    if ($LASTEXITCODE -ne 0) { throw "artifact manifest root resolution failed" }

    foreach ($texFile in $roots) {
        if (-not [string]::IsNullOrWhiteSpace($texFile)) {
            $label = [System.IO.Path]::GetFileNameWithoutExtension($texFile)
            Invoke-CvTexBuild -TexFile $texFile -Label $label
        }
    }

    & python tools/artifact_manifest.py publish
    if ($LASTEXITCODE -ne 0) { throw "artifact publication failed" }
} finally {
    Pop-Location
}
