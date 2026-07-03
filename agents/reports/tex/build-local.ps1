<#
.SYNOPSIS
    Local LaTeX build script for AgenticCareerBoost reports.

.DESCRIPTION
    Builds report PDFs locally and delegates publication filtering/copying to
    tools/publish-public-reports.py, the same publisher used by CI.
#>

param(
    [ValidateSet("all", "s000", "guide", "smoke", "clean")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$texRoot = $PSScriptRoot

function Test-LatexmkWorks {
    try {
        & latexmk --version | Out-Null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Invoke-PdflatexBuild {
    param([string]$TexFile)

    if (-not (Test-Path "build")) {
        New-Item -ItemType Directory -Path "build" -Force | Out-Null
    }
    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "  pass $pass/3..." -ForegroundColor DarkGray
        & pdflatex -interaction=nonstopmode -halt-on-error -output-directory=build -aux-directory=build $TexFile | Out-Null
        if ($LASTEXITCODE -ne 0) {
            return $false
        }
    }
    return $true
}

function Invoke-LatexmkBuild {
    param([string]$TexFile)

    & latexmk -r latexmkrc -pdf -interaction=nonstopmode -halt-on-error $TexFile
    return $LASTEXITCODE -eq 0
}

function Publish-ReportPdf {
    param([string]$TexFile)

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($TexFile)
    $pdf = Join-Path "build" "$baseName.pdf"
    & python "tools/publish-public-reports.py" $pdf
    if ($LASTEXITCODE -ne 0) {
        throw "Public report publishing failed for $pdf"
    }
}

function Build-TexFile {
    param([string]$TexFile, [string]$Label)

    Write-Host "[build-local] Building $Label..." -ForegroundColor Cyan
    if ($script:useLatexmk) {
        $ok = Invoke-LatexmkBuild -TexFile $TexFile
    } else {
        $ok = Invoke-PdflatexBuild -TexFile $TexFile
    }

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($TexFile)
    $pdf = Join-Path "build" "$baseName.pdf"
    if (-not $ok -or -not (Test-Path $pdf)) {
        Write-Host "[build-local] FAILED: $Label" -ForegroundColor Red
        return $false
    }

    $size = [math]::Round((Get-Item $pdf).Length / 1KB)
    Write-Host "[build-local] OK: $pdf ($size KB)" -ForegroundColor Green
    Publish-ReportPdf -TexFile $TexFile
    return $true
}

function Build-TexFiles {
    param([object[]]$TexFiles)

    if (-not $TexFiles -or $TexFiles.Count -eq 0) {
        Write-Warning "No .tex files found."
        return $true
    }

    $failed = 0
    foreach ($f in $TexFiles) {
        $ok = Build-TexFile -TexFile $f.FullName -Label $f.Name
        if (-not $ok) { $failed++ }
    }
    return $failed -eq 0
}

Push-Location $texRoot
try {
    if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
        Write-Error "pdflatex not found. Install TeX Live or MiKTeX and ensure it is on your PATH."
        exit 1
    }

    $script:useLatexmk = Test-LatexmkWorks
    if ($script:useLatexmk) {
        Write-Host "[build-local] Engine: latexmk" -ForegroundColor DarkGray
    } else {
        Write-Host "[build-local] Engine: pdflatex" -ForegroundColor DarkGray
    }

    switch ($Target) {
        "clean" {
            Write-Host "[build-local] Cleaning build artifacts..." -ForegroundColor Yellow
            if ($script:useLatexmk) { latexmk -r latexmkrc -C 2>$null }
            if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
            Write-Host "[build-local] Clean complete." -ForegroundColor Green
        }
        "smoke" {
            if (-not (Build-TexFile -TexFile "smoke.tex" -Label "smoke test")) { exit 1 }
        }
        "s000" {
            if (-not (Build-TexFile -TexFile "sprints/s000-agentic-os-bootstrap.tex" -Label "Sprint S-000")) { exit 1 }
        }
        "guide" {
            if (-not (Build-TexFile -TexFile "guides/agentic-system-guide.tex" -Label "Agentic system guide")) { exit 1 }
        }
        "all" {
            $sprintFiles = Get-ChildItem -Path "sprints" -Filter "*.tex" -ErrorAction SilentlyContinue
            $guideFiles = Get-ChildItem -Path "guides" -Filter "*.tex" -ErrorAction SilentlyContinue
            if (-not (Build-TexFiles -TexFiles @($sprintFiles + $guideFiles))) { exit 1 }
        }
    }
} finally {
    Pop-Location
}
