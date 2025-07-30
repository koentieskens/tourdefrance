@echo off
echo Creating executable with dependencies...

:: Activate the virtual environment
call .venv\Scripts\activate.bat

:: Ensure all required packages are installed
pip install pyinstaller pandas lxml

:: Create the executable with additional DLL collection
pyinstaller --onefile ^
    --add-data "tdf2025_startlist.csv;." ^
    --console ^
    --name open_rider ^
    --hidden-import pandas ^
    --collect-all pandas ^
    --collect-all numpy ^
    open_pagew.py

if errorlevel 1 (
    echo Failed to create executable
    pause
    exit /b 1
)

echo.
echo Executable created successfully! Check the 'dist' folder.
echo.
pause
