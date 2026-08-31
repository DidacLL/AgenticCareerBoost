@ECHO OFF
SETLOCAL
TITLE Local site launcher
CD /D "%~dp0site"
node --version >NUL 2>&1
IF ERRORLEVEL 1 (
  ECHO Node.js 22.12 or newer is required.
  EXIT /B 1
)
FOR /F "tokens=1,2 delims=." %%A IN ('node -p "process.versions.node"') DO (
  SET NODE_MAJOR=%%A
  SET NODE_MINOR=%%B
)
IF %NODE_MAJOR% LSS 22 (
  ECHO Node.js 22.12 or newer is required.
  EXIT /B 1
)
IF %NODE_MAJOR% EQU 22 IF %NODE_MINOR% LSS 12 (
  ECHO Node.js 22.12 or newer is required.
  EXIT /B 1
)
IF NOT EXIST "node_modules\astro" (
  ECHO Installing site dependencies...
  npm install --no-package-lock
  IF ERRORLEVEL 1 EXIT /B 1
)
npm run dev -- --open
