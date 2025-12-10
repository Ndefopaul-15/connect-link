@echo off
echo Fixing invalid slugs in database...
echo.

call .venv\Scripts\activate.bat
python fix_invalid_slugs.py

pause
