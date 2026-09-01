<#
.SYNOPSIS
    Build public career PDFs from agents/cv/artifacts.json.
#>

$ErrorActionPreference = "Stop"
$cvRoot = $PSScriptRoot
$texRoot = Join-Path $cvRoot "tex"
$buildRoot = Join-Path $cvRoot "build"

function Test-LatexmkWorks {
    try {
        & latexmk --version *> $null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Remove-CvTexAuxiliaries {
    param([string]$BaseName)

    $suffixes = @(
        ".aux", ".log", ".out", ".fls", ".fdb_latexmk", ".synctex.gz",
        ".toc", ".lof", ".lot", ".nav", ".snm", ".vrb",
        ".bbl", ".bcf", ".blg", ".run.xml", ".xdv"
    )
    foreach ($suffix in $suffixes) {
        $path = Join-Path $texRoot ($BaseName + $suffix)
        if (Test-Path $path) {
            Remove-Item -Force $path
        }
    }
}

function Invoke-CvTexBuild {
    param([string]$TexFile)

    $sourceName = [System.IO.Path]::GetFileName($TexFile)
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($TexFile)
    Remove-CvTexAuxiliaries -BaseName $baseName

    Write-Host "[cv-build] Building $baseName..." -ForegroundColor Cyan
    if (-not (Test-Path $buildRoot)) {
        New-Item -ItemType Directory -Path $buildRoot -Force | Out-Null
    }

    Push-Location $texRoot
    try {
        if ($script:useLatexmk) {
            & latexmk -r ../latexmkrc -pdf -interaction=nonstopmode -halt-on-error -outdir=../build -auxdir=../build $sourceName
            if ($LASTEXITCODE -ne 0) { throw "latexmk failed for $sourceName" }
            return
        }

        $pdfArgs = @(
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory=../build",
            $sourceName
        )
        for ($pass = 1; $pass -le 3; $pass++) {
            Write-Host "  pass $pass/3..." -NoNewline -ForegroundColor DarkGray
            & pdflatex @pdfArgs *> $null
            if ($LASTEXITCODE -ne 0) {
                Write-Host " FAILED" -ForegroundColor Red
                throw "pdflatex failed for $sourceName"
            }
            Write-Host " ok" -ForegroundColor DarkGray
        }
    } finally {
        Pop-Location
        Remove-CvTexAuxiliaries -BaseName $baseName
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

    $roots = & python tools/artifact_manifest.py roots
    if ($LASTEXITCODE -ne 0) { throw "artifact manifest root resolution failed" }

    foreach ($texFile in $roots) {
        if (-not [string]::IsNullOrWhiteSpace($texFile)) {
            Invoke-CvTexBuild -TexFile $texFile
        }
    }

    & python tools/artifact_manifest.py publish
    if ($LASTEXITCODE -ne 0) { throw "artifact publication failed" }
    Write-Host "[cv-build] Done. Generated files are under agents/cv/build/." -ForegroundColor Green
} finally {
    Pop-Location
}
