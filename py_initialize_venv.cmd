@echo off

echo Create empty venv
IF EXIST "venv" rd /s /q venv
python3.8 -m venv venv

rem Activate virtual environment:
call venv\Scripts\activate.bat

echo Installing requirements...
python -m pip install --upgrade pip
pip install -r requirements.txt

call venv\Scripts\deactivate.bat
:END