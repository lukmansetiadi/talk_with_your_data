@echo off
setlocal enabledelayedexpansion

echo ==================================================
echo  🚀 AI SQL Agent: GitHub Update Script
echo ==================================================

REM Check if there are any changes to commit
git status --short | findstr /R "^" >nul
if %errorlevel% neq 0 (
    echo.
    echo ✅ No changes detected. Workspace is clean.
    goto :END
)

echo.
echo 📦 Staging all changes...
git add .

REM Ask for a commit message or use a default one
set /p commit_msg="📝 Enter commit message (leave blank for 'Feature: AI Query Recommendations, Default Templates, and Multi-Query Execution'): "
if "!commit_msg!"=="" set commit_msg=Feature: AI Query Recommendations, Default Templates, and Multi-Query Execution

echo.
echo 💾 Committing changes...
git commit -m "!commit_msg!"

echo.
echo 📤 Pushing to GitHub (origin main)...
echo.

:PUSH
git push origin main

if %errorlevel% equ 0 (
    echo.
    echo ==================================================
    echo ✨ Push successful! Your code is now live on GitHub.
    echo ==================================================
) else (
    echo.
    echo ❌ Push failed. 
    set /p retry="🔄 Would you like to retry the push? (y/n): "
    if /i "!retry!"=="y" (
        echo.
        echo 📤 Retrying push...
        goto :PUSH
    )
)

:END
echo.
pause
