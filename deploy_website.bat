@echo off
echo Checking if remote repository exists...
git ls-remote origin >nul 2>&1
if errorlevel 1 (
    echo Adding remote repository...
    git remote add origin https://github.com/%1/%1.github.io.git
) else (
    echo Remote repository already exists.
)

echo Pulling remote repository...
git pull origin main --allow-unrelated-histories
echo Adding website files to the Git repository...
git add .
echo Committing the changes...
git commit -m "Update website"
echo Pushing the changes to GitHub...
git push origin main
echo Deployment completed.
pause

