# Puzzle Game
## Installation steps
### 1. Requirements
1. Make sure that you have installed python 3.8 on your computer.
2. Code is tested under Windows environment.
### 2. Source code installation and run
1. After installation of source you can simply run cmd to initialize you virtual environment:
```
py_initialize_venv.cmd
```
2. After successful environment installation you can simply run puzzle game
```
run.cmd
```
### 3. Alternative way to install the game
In the root of directory you can find distribution directory 'dist'. Inside this directory you can find .whl file of this game.
It's built python package which can be easily installed using:
```
pip install pazzle_game-0.0.1-py3-none-any.whl
```
After this you can use this game from code and run it with:
```
from game.core.puzzle_game import PuzzleGame
from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum

if __name__ == '__main__':
    game = PuzzleGame()
    game.run_game(x_size=2, y_size=3, difficulty=PuzzleDifficultyEnum.Hard)
```
## Game rules
Using rules is straight forward. You need to click on A,W,S,D to control the empty square.
If you want to finish the game press Q.
Keys are case-independent.
## Game parameters
There are 3 main game parameters : x_size, y_size - it's the game size parameters.
You can specify your own size for game(not only 4*4).
And exist parameter difficulty. There are 3 main options of this parameter - Easy, Medium and Hard.
This parameter take part in shuffling.

This parameters can be passed to run_game() function in order you running it as python wheel.
But also exist settings.json in the root of repo which you can override to run custom version of game.
## Testing stage
To comfortable testing provided coverage report. Which shows us results of testing and also rate of code coverage.
To run this report you need to do several steps:
```
cd test_coverage
create-report.cmd
```
After this in logs you will see detailed information.
Also coverage rete you can open in browser using index.html inside html_report directory.
## Building wheel after modifications.
To build new version of wheel you need simply run corresponding command:
```
build_wheel.cmd
```





