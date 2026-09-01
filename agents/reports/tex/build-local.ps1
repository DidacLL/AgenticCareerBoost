<#
.SYNOPSIS
    Local LaTeX build script for AgenticCareerBoost reports.
    Mirrors the CI pipeline (.github/workflows/latex-build.yml).

.DESCRIPTION
    Compiles all report documents (sprints and guides, or a specific one)
    using pdflatex.
    Uses latexmk if available (requires Perl); otherwise falls back to
    multi-pass pdflatex directly. Run this before committing to verify
    the PDF output locally.

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

    # Three passes: (1) initial, (2) resolve references, (3) final
    for ($pass = 1; $pass -le 3; $pass++) {
        Write-Host "  pass $pass/3..." -ForegroundColor DarkGray -NoNewline
        $proc = Start-Process -FilePath "pdflatex" -ArgumentList $pdfArgs `
            -NoNewWindow -Wait -PassThru -RedirectStandardOutput "NUL" 2>&1
        if ($proc.ExitCode -ne 0) {
            Write-Host " FAILED" -ForegroundColor Red
            Write-Host "`n  Check the log at: $BuildDir\$([System.IO.Path]::GetFileNameWithoutExtension($TexFile)).log" -ForegroundColor Yellow
            # Show the last error from the log
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

    if ($script:useLatexmk) {
        $ok = Invoke-Latexmk -TexFile $TexFile
    } else {
        $ok = Invoke-Pdflatex -TexFile $TexFile -BuildDir "build"
    }

    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($TexFile)
    $pdf = Join-Path "build" "$baseName.pdf"

    if ($ok -and (Test-Path $pdf)) {
        $size = [math]::Round((Get-Item $pdf).Length / 1KB)
        Write-Host "[build-local] OK: $pdf ($size KB)" -ForegroundColor Green
        return $true
    } else {
        Write-Host "[build-local] FAILED: $Label" -ForegroundColor Red
        return $false
    }
}

function Build-TexFiles {
    param(
        [object[]]$TexFiles,
        [string]$Label
    )

    if (-not $TexFiles -or $TexFiles.Count -eq 0) {
        Write-Warning "No .tex files found for $Label"
        return $true
    }

    $failed = 0
    foreach ($f in $TexFiles) {
        $ok = Build-TexFile -TexFile $f.FullName -Label $f.Name
        if (-not $ok) { $failed++ }
    }

    if ($failed -gt 0) {
        Write-Host "`n[build-local] $failed file(s) failed." -ForegroundColor Red
        return $false
    }

    return $true
}

# --- Main ---
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
        Write-Host "[build-local] Engine: pdflatex (3-pass, latexmk unavailable)" -ForegroundColor DarkGray
    }

    switch ($Target) {
        "clean" {
            Write-Host "[build-local] Cleaning build artifacts..." -ForegroundColor Yellow
            if ($script:useLatexmk) {
                latexmk -r latexmkrc -C 2>$null
            }
            if (Test-Path "build") { Remove-Item -Recurse -Force "build" }
            Write-Host "[build-local] Clean complete." -ForegroundColor Green
        }
        "smoke" {
            $ok = Build-TexFile -TexFile "smoke.tex" -Label "smoke test"
            if (-not $ok) { exit 1 }
        }
        "s000" {
            $ok = Build-TexFile -TexFile "sprints/s000-agentic-os-bootstrap.tex" -Label "Sprint S-000"
            if (-not $ok) { exit 1 }
        }
        "guide" {
            $ok = Build-TexFile -TexFile "guides/agentic-system-guide.tex" -Label "Agentic system guide"
            if (-not $ok) { exit 1 }
        }
        "all" {
            $sprintFiles = Get-ChildItem -Path "sprints" -Filter "*.tex" -ErrorAction SilentlyContinue
            $guideFiles = Get-ChildItem -Path "guides" -Filter "*.tex" -ErrorAction SilentlyContinue
            $ok = Build-TexFiles -TexFiles @($sprintFiles + $guideFiles) -Label "all report documents"
            if (-not $ok) { exit 1 }
        }
    }
} finally {
    Pop-Location
}
