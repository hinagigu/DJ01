@echo off
title UI Generator

cd /d "%~dp0"

echo ========================================
echo           UI Generator Tool
echo ========================================
echo.

python main.py

if %errorlevel% neq 0 (
    echo.
    echo [Error] Program exited with code: %errorlevel%
    pause
)