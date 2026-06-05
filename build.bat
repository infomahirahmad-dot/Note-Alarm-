@echo off
title Note Alarm - Build Script
color 0A

echo ============================================
echo   Note Alarm - .EXE Builder
echo ============================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found! Please install Python 3.8+
    echo Download: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo [1/4] Installing required packages...
pip install pywebview pyinstaller --quiet
if errorlevel 1 (
    echo [ERROR] Package installation failed!
    pause
    exit /b 1
)

echo [2/4] Cleaning previous build...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist

echo [3/4] Building NoteAlarm.exe...
pyinstaller NoteAlarm.spec --clean --noconfirm
if errorlevel 1 (
    echo [ERROR] Build failed! Check the error above.
    pause
    exit /b 1
)

echo [4/4] Done!
echo.
echo ============================================
echo   SUCCESS! Your app is ready:
echo   dist\NoteAlarm.exe
echo ============================================
echo.

if exist dist\NoteAlarm.exe (
    echo Do you want to run it now? (Y/N)
    set /p choice=
    if /i "%choice%"=="Y" start dist\NoteAlarm.exe
)

pause
