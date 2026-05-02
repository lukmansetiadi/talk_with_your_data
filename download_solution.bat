@echo off
echo Downloading Python solution from GitHub...

git clone https://github.com/lukmansetiadi/talk_with_your_data.git

if %errorlevel% equ 0 (
    echo.
    echo Successfully downloaded the solution!
) else (
    echo.
    echo Error downloading repository. Please make sure Git is installed on your system.
)

pause