@echo off
cls
echo ===================================================
echo     INITIALIZING AUTOMATED PRODUCTION DEPLOYMENT   
echo ===================================================

echo [1/4] Syncing cloud tracking branches...
git pull origin main --rebase

set /p milestone="Enter the completed Lecture Number (e.g., 60): "

echo.
echo [2/4] Executing background text engine pipeline...
python update_readme.py %milestone%

echo.
echo [3/4] Staging changes and logging architecture commitments...
git add .
git commit -m "Udemy: Completed Lecture %milestone% / 161"

echo.
echo [4/4] Deploying pristine assets straight to GitHub live branch...
git push origin main

echo.
echo ===================================================
echo   DEPLOYMENT SUCCESSFUL! DISCONNECTING PIPELINE.   
echo ===================================================
pause
