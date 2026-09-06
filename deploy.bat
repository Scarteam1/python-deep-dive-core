@echo off
cls
echo ===================================================
echo     INITIALIZING AUTOMATED PRODUCTION DEPLOYMENT   
echo ===================================================

echo [1/4] Syncing cloud tracking branches...
git pull origin main --rebase

set /p milestone="Enter the completed Lecture Number (e.g., 44): "

echo.
echo [2/4] Advancing visual portfolio README dashboard matrix to Lecture %milestone%...
python -c "import re; f=open('README.md', 'r', encoding='utf-8'); c=f.read(); f.close(); u=re.sub(r'\d+ / 161 Lectures Completed', f'%milestone% / 161 Lectures Completed', c); u=re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-%milestone%)', u); f=open('README.md', 'w', encoding='utf-8'); f.write(u); f.close()"

echo.
echo [3/4] Staging changes and logging architecture milestone commitments...
git add .
git commit -m "Udemy: Completed Lecture %milestone% / 161" -m "Automated systems infrastructure sync pipeline execution tracking progress milestones."

echo.
echo [4/4] Deploying pristine assets straight to GitHub live branch...
git push origin main

echo.
echo ===================================================
echo   DEPLOYMENT SUCCESSFUL! DISCONNECTING PIPELINE.   
echo ===================================================
pause
