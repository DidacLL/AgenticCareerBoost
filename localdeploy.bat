@ECHO OFF
TITLE Local site launcher
ECHO --- Open site ---
START "" "http://localhost:8765"
ECHO --- Launching server ---
ECHO.
py -m http.server 8765 -d site
