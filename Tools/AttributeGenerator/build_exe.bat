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

echo [1/4] Checking PyInstaller...
pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo       Installing PyInstaller...
    pip install pyinstaller
)

cd /d "%~dp0"

echo [2/4] Cleaning old build files...
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "DJ01_GAS_Generator.spec" del /q "DJ01_GAS_Generator.spec"

echo [3/4] Building exe...
echo       Including modules: main, config, ui_base, attribute, execution, mmc, tag
pyinstaller --onefile --windowed --name "DJ01_GAS_Generator" ^
    --collect-submodules=ui_base ^
    --collect-submodules=attribute ^
    --collect-submodules=execution ^
    --collect-submodules=mmc ^
    --collect-submodules=tag ^
    --hidden-import=config ^
    main.py

echo [4/4] Finalizing...
if exist "dist\DJ01_GAS_Generator.exe" (
    copy /Y "dist\DJ01_GAS_Generator.exe" "..\.." >nul
    echo.
    echo ============================================================
    echo [SUCCESS] Generated: DJ01_GAS_Generator.exe
    echo           Location: Project root directory
    echo ============================================================
) else (
    echo.
    echo [ERROR] Build failed. Check the output above for details.
    pause
    exit /b 1
)

echo.
echo Cleaning up temporary files...
if exist "build" rd /s /q "build"
if exist "dist" rd /s /q "dist"
if exist "DJ01_GAS_Generator.spec" del /q "DJ01_GAS_Generator.spec"

echo Done!
echo.
pause