@echo off
setlocal
set "SCRIPT_DIR=%~dp0"
py -3 "%SCRIPT_DIR%start_tracker.py" --mode readonly
if errorlevel 1 python "%SCRIPT_DIR%start_tracker.py" --mode readonly
if errorlevel 1 pause
