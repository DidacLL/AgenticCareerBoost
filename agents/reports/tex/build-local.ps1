<#
.SYNOPSIS
    Local LaTeX build script for AgenticCareerBoost report evidence.
.DESCRIPTION
    Compiles report documents into agents/reports/tex/build/. Reports are
    repository evidence and are not copied into the portfolio tree.
#>

param(
    [ValidateSet("all", "s000", "guide", "smoke", "clean")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$texRoot = $PSScriptRoot

function Test-LatexmkWorks {
    try {
        & latexmk --version *> $null
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Invoke-Pdflatex {
    param([string]$TexFile, [string]$BuildDir)
    if (-not (Test-Path $BuildDir)) { New-Item -ItemType Directory -Path $BuildDir -Force | Out-Null }
    $pdfArgs = @("-interaction=nonstopmode", "-halt-on-error", "-output-directory=$BuildDir", "-aux-directory=$BuildDir", $TexFile)
    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "  pass $pass/3..." -ForegroundColor DarkGray -NoNewline
        $proc = Start-Process -FilePath "pdflatex" -ArgumentList $pdfArgs -NoNewWindow -Wait -PassThru -RedirectStandardOutput "NUL" 2>&1
        if ($proc.ExitCode -ne 0) {
            Write-Host " FAILED" -ForegroundColor Red
            Write-Host "Check build/$([System.IO.Path]::GetFileNameWithoutExtension($TexFile)).log" -ForegroundColor Yellow
            return $false
        }
        Write-Host " ok" -ForegroundColor DarkGray
    }
    return $true
}

function Invoke-Latexmk {
    param([string]$TexFile)
    & latexmk -r latexmkrc -pdf -interaction=nonstopmode -halt-on-error $TexFile
    return $LASTEXITCODE -eq 0
}

function Build-TexFile {
    param([string]$TexFile, [string]$Label)
    Write-Host "[build-local] Building $Label..." -ForegroundColor Cyan
    $ok = if ($script:useLatexmk) { Invoke-Latexmk -TexFile $TexFile } else { Invoke-Pdflatex -TexFile $TexFile -BuildDir "build" }
    $pdf = Join-Path "build" "$([System.IO.Path]::GetFileNameWithoutExtension($TexFile)).pdf"
    if ($ok -and (Test-Path $pdf)) {
        $size = [math]::Round((Get-Item $pdf).Length / 1KB)
        Write-Host "[build-local] OK: $pdf ($size KB)" -ForegroundColor Green
        return $true
    }
    Write-Host "[build-local] FAILED: $Label" -ForegroundColor Red
    return $false
}

function Build-TexFiles {
    param([object[]]$TexFiles)
    $failed = 0
    foreach ($f in $TexFiles) { if (-not (Build-TexFile -TexFile $f.FullName -Label $f.Name)) { $failed++ } }
    return $failed -eq 0
}

Push-Location $texRoot
try {
    if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
        Write-Error "pdflatex not found. Install TeX Live or MiKTeX and ensure it is on PATH."
        exit 1
    }
    $script:useLatexmk = Test-LatexmkWorks
    switch ($Target) {
        "clean" {
            if ($script:useLatexmk) { latexmk -r latexmkrc -C 2>$null }
            if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
        }
        "smoke" { if (-not (Build-TexFile -TexFile "smoke.tex" -Label "smoke test")) { exit 1 } }
        "s000" { if (-not (Build-TexFile -TexFile "sprints/s000-agentic-os-bootstrap.tex" -Label "Sprint S-000")) { exit 1 } }
        "guide" { if (-not (Build-TexFile -TexFile "guides/agentic-system-guide.tex" -Label "Agentic system guide")) { exit 1 } }
        "all" {
            $files = @(Get-ChildItem -Path "sprints" -Filter "*.tex" -ErrorAction SilentlyContinue) + @(Get-ChildItem -Path "guides" -Filter "*.tex" -ErrorAction SilentlyContinue)
            if (-not (Build-TexFiles -TexFiles $files)) { exit 1 }
        }
    }
    Write-Host "[build-local] Report PDFs remain under agents/reports/tex/build/." -ForegroundColor DarkGray
} finally {
    Pop-Location
}