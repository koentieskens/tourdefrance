@echo off
echo Checking for virtual environment...

:: First, check if venv directory exists in current folder
IF EXIST "venv\Scripts\activate.bat" (
    set VENV_PATH=venv
) ELSE IF EXIST ".venv\Scripts\activate.bat" (
    set VENV_PATH=.venv
) ELSE (
    echo Virtual environment not found in current directory.
    echo Please ensure you have a virtual environment set up.
    echo Expected locations: .\venv or .\.venv
    echo.
    echo Current directory contents:
    dir /b
    pause
    exit /b 1
)

echo Found virtual environment at: %VENV_PATH%
echo.

:: Activate the virtual environment
call "%VENV_PATH%\Scripts\activate.bat"

:: Check if activation was successful
if errorlevel 1 (
    echo Failed to activate virtual environment
    pause
    exit /b 1
)

:: Verify Python is using the correct environment
where python
python --version

:: Install pyinstaller if not already installed
pip install pyinstaller

:: Create the executable
pyinstaller --onefile ^
    --add-data "tdf2025_startlist.csv;." ^
    --console ^
    --name open_rider ^
    --hidden-import pandas ^
    --hidden-import webbrowser ^
    --hidden-import lxml ^
    get_name_standalone.py

:: Check if executable creation was successful
if errorlevel 1 (
    echo Failed to create executable
    pause
    exit /b 1
)

echo.
echo Executable created successfully! Check the 'dist' folder.
echo.
pause
