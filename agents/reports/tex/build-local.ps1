<#
.SYNOPSIS
    Local LaTeX build script for AgenticCareerBoost reports.
    Mirrors the dedicated report CI pipeline.

.DESCRIPTION
    Compiles all report documents (sprints and guides, or a specific one)
    using pdflatex. Uses latexmk if available (requires Perl); otherwise falls
    back to multi-pass pdflatex directly. Generated PDFs remain under build/;
    report builds do not publish files into the portfolio.

.PARAMETER Target
    Which document to build:
      all    - all sprints/*.tex and guides/*.tex files (default)
      s000   - Sprint S-000 document only
      guide  - Agentic system guide only
      smoke  - preamble smoke test only
      clean  - remove build artifacts

.EXAMPLE
    .\build-local.ps1
    .\build-local.ps1 -Target s000
    .\build-local.ps1 -Target smoke
    .\build-local.ps1 -Target clean
#>

param(
    [ValidateSet("all", "s000", "guide", "smoke", "clean")]
    [string]$Target = "all"
)

$ErrorActionPreference = "Stop"
$texRoot = $PSScriptRoot

function Test-LatexmkWorks {
    try {
        $out = & latexmk --version 2>&1
        return $LASTEXITCODE -eq 0
    } catch {
        return $false
    }
}

function Invoke-Pdflatex {
    param([string]$TexFile, [string]$BuildDir)

    if (-not (Test-Path $BuildDir)) {
        New-Item -ItemType Directory -Path $BuildDir -Force | Out-Null
    }

    $pdfArgs = @(
        "-interaction=nonstopmode",
        "-halt-on-error",
        "-output-directory=$BuildDir",
        "-aux-directory=$BuildDir",
        $TexFile
    )

    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "  pass $pass/3..." -ForegroundColor DarkGray -NoNewline
        $proc = Start-Process -FilePath "pdflatex" -ArgumentList $pdfArgs `
            -NoNewWindow -Wait -PassThru -RedirectStandardOutput "NUL" 2>&1
        if ($proc.ExitCode -ne 0) {
            Write-Host " FAILED" -ForegroundColor Red
            Write-Host "`n  Check the log at: $BuildDir\$([System.IO.Path]::GetFileNameWithoutExtension($TexFile)).log" -ForegroundColor Yellow
            $logFile = Join-Path $BuildDir "$([System.IO.Path]::GetFileNameWithoutExtension($TexFile)).log"
            if (Test-Path $logFile) {
                $logLines = Get-Content $logFile
                $errorLines = $logLines | Where-Object { $_ -match "^!" }
                if ($errorLines) {
                    Write-Host "`n  Errors found:" -ForegroundColor Red
                    $errorLines | ForEach-Object { Write-Host "    $_" -ForegroundColor Red }
                }
            }
            return $false
        }
        Write-Host " ok" -ForegroundColor DarkGray
    }
    return $true
}

function Invoke-Latexmk {
    param([string]$TexFile)

    $lmkArgs = @(
        "-r", "latexmkrc",
        "-pdf",
        "-interaction=nonstopmode",
        "-halt-on-error",
        $TexFile
    )
    & latexmk @lmkArgs
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
    param([object[]]$TexFiles, [string]$Label)

    if (-not $TexFiles -or $TexFiles.Count -eq 0) {
        Write-Warning "No .tex files found for $Label"
        return $true
    }

    $failed = 0
    foreach ($f in $TexFiles) {
        if (-not (Build-TexFile -TexFile $f.FullName -Label $f.Name)) { $failed++ }
    }
    if ($failed -gt 0) {
        Write-Host "`n[build-local] $failed file(s) failed." -ForegroundColor Red
        return $false
    }
    return $true
}

Push-Location $texRoot
try {
    if (-not (Get-Command pdflatex -ErrorAction SilentlyContinue)) {
        Write-Error "pdflatex not found. Install TeX Live or MiKTeX and ensure it is on PATH."
        exit 1
    }

    $script:useLatexmk = Test-LatexmkWorks
    if ($script:useLatexmk) {
        Write-Host "[build-local] Engine: latexmk" -ForegroundColor DarkGray
    } else {
        Write-Host "[build-local] Engine: pdflatex (3-pass, latexmk unavailable)" -ForegroundColor DarkGray
    }

    switch ($Target) {
        "clean" {
            Write-Host "[build-local] Cleaning build artifacts..." -ForegroundColor Yellow
            if ($script:useLatexmk) { latexmk -r latexmkrc -C 2>$null }
            if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
            Write-Host "[build-local] Clean complete." -ForegroundColor Green
        }
        "smoke" { if (-not (Build-TexFile -TexFile "smoke.tex" -Label "smoke test")) { exit 1 } }
        "s000" { if (-not (Build-TexFile -TexFile "sprints/s000-agentic-os-bootstrap.tex" -Label "Sprint S-000")) { exit 1 } }
        "guide" { if (-not (Build-TexFile -TexFile "guides/agentic-system-guide.tex" -Label "Agentic system guide")) { exit 1 } }
        "all" {
            $sprintFiles = Get-ChildItem -Path "sprints" -Filter "*.tex" -ErrorAction SilentlyContinue
            $guideFiles = Get-ChildItem -Path "guides" -Filter "*.tex" -ErrorAction SilentlyContinue
            if (-not (Build-TexFiles -TexFiles @($sprintFiles + $guideFiles) -Label "all report documents")) { exit 1 }
        }
    }
    Write-Host "[build-local] Report PDFs remain under agents/reports/tex/build/." -ForegroundColor DarkGray
} finally {
    Pop-Location
}
