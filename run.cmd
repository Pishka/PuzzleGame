set GAME_PYTHON_PATH=.\src
set PYTHONPATH=%GAME_PYTHON_PATH%;%PYTHONPATH%

call venv\Scripts\activate.bat
python -m game.cmd.run_game_cmd
call venv\Scripts\deactivate.bat