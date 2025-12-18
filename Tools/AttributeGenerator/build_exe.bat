@echo off
chcp 65001 >nul
echo ============================================================
echo DJ01 GAS Code Generator - Build Tool
echo ============================================================
echo.

python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo [1/3] Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo       Installing PyInstaller...
    pip install pyinstaller
)

cd /d "%~dp0"

echo [2/3] Building exe...
pyinstaller --onefile --windowed --name "DJ01_GAS_Generator" main.py

echo [3/3] Cleaning up...
if exist "dist\DJ01_GAS_Generator.exe" (
    copy /Y "dist\DJ01_GAS_Generator.exe" "..\.." >nul
    echo.
    echo ============================================================
    echo [SUCCESS] Generated: DJ01_GAS_Generator.exe
    echo           Location: Project root directory
    echo ============================================================
) else (
    echo [ERROR] Build failed
)

if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "DJ01_GAS_Generator.spec" del /q "DJ01_GAS_Generator.spec"

echo.
pause