@echo off
cls
echo [1/3] Syncing...
git pull origin main --rebase
set /p milestone="Enter Lecture Number: "
python -c "import re; f=open('README.md', 'r', encoding='utf-8'); c=f.read(); f.close(); u=re.sub(r'Current Progress:\s*.*?\s*\d+ / 161', f'Current Progress: 🟩🟩🟩🟩🟩🟩🟪🟪🟪🟪 59 / 161', c); u=re.sub(r'\(Lectures 31-\d+\)', f'(Lectures 31-59)', u); f=open('README.md', 'w', encoding='utf-8'); f.write(u); f.close()"
git add .
git commit -m "Udemy: Completed Lecture 59 / 161"
git push origin main
echo Done!
pause
