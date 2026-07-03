<#
.SYNOPSIS
    Build public CV and public-safe cover-letter PDFs.
#>

$ErrorActionPreference = "Stop"
$cvRoot = $PSScriptRoot
$repoRoot = Resolve-Path (Join-Path $cvRoot "..\..")
$publicCvDir = Join-Path $repoRoot "site\files\cv"
$publicLetterDir = Join-Path $repoRoot "site\files\cover-letters"

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
    & python tools/render-cover-letter.py --all
    if (-not (Test-Path $publicCvDir)) { New-Item -ItemType Directory -Path $publicCvDir -Force | Out-Null }
    if (-not (Test-Path $publicLetterDir)) { New-Item -ItemType Directory -Path $publicLetterDir -Force | Out-Null }

    Invoke-CvTexBuild -TexFile "tex/didac-llorens-cv.tex" -Label "CV"
    Copy-Item -LiteralPath "build\didac-llorens-cv.pdf" -Destination (Join-Path $publicCvDir "didac-llorens-cv.pdf") -Force
    Write-Host "[cv-build] Published: site\files\cv\didac-llorens-cv.pdf" -ForegroundColor Green

    Get-ChildItem -LiteralPath "build\generated" -Filter "*.tex" | ForEach-Object {
        $baseName = [System.IO.Path]::GetFileNameWithoutExtension($_.Name)
        Invoke-CvTexBuild -TexFile $_.FullName -Label $baseName
        Copy-Item -LiteralPath "build\$baseName.pdf" -Destination (Join-Path $publicLetterDir "$baseName.pdf") -Force
        Write-Host "[cv-build] Published: site\files\cover-letters\$baseName.pdf" -ForegroundColor Green
    }
} finally {
    Pop-Location
}
