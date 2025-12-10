@echo off
echo.
echo ========================================
echo   Password Reset Database Update
echo ========================================
echo.

call .venv\Scripts\activate.bat
python update_database.py
pause
