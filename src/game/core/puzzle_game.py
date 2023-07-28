from typing import Optional

import os
import attr
from attr import dataclass
import keyboard

from game.core.utils.puzzle_valid_moves_enum import PuzzleValidMovesEnum
from game.core.puzzle_game_settings import PuzzleGameSettings
from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum
from game.core.puzzle_board import PuzzleBoard


@dataclass
class PuzzleGame:
    """Class that manipulates on the game."""

    board: PuzzleBoard = attr.ib(default=None, kw_only=True)
    """Game board."""

    def run_game(self, x_size: Optional[int]=None, y_size: Optional[int]=None, difficulty: Optional[PuzzleDifficultyEnum]=None):
        """Run game till the end."""
        # Init board setup
        self._start_game(x_size=x_size, y_size=y_size, difficulty=difficulty)
        # Run the game till not solved or user don't quit
        while not self.is_game_finished():
            # Snapshot game view
            self._game_frame_view()
            # Run re-input while user will not proceed with correct move
            is_valid_move = False
            # Possible key presses
            valid_moves = [e.name for e in PuzzleValidMovesEnum]
            while not is_valid_move:
                # check which key was pressed
                for key in valid_moves:
                    # check both lower and upper case
                    if keyboard.is_pressed(key.lower()) or keyboard.is_pressed(key.upper()):
                        # Skip key chain
                        while keyboard.is_pressed(key.lower()) or keyboard.is_pressed(key.upper()):
                            continue
                        # End game in case of q is pressed
                        if PuzzleValidMovesEnum[key.lower()] == PuzzleValidMovesEnum.q:
                            return
                        # Try to proceed with moving
                        try:
                            direction = PuzzleValidMovesEnum[key.lower()]
                            self.board.move(direction)
                            is_valid_move = True
                        except IndexError:
                            print(f"{key.upper()} is not valid move. You out of border. Please choose another one.")
        # Result board view
        self._game_frame_view()
        print("You solved the puzzle. Congratulations!!!")

    def is_game_finished(self) -> bool:
        """Returns True if game is finished(solved) by user."""
        return self.board.board_solved()

    def _start_game(self, x_size: Optional[int]=None, y_size: Optional[int]=None, difficulty: Optional[PuzzleDifficultyEnum]=None):
        """Method to run initial setup of board and start game."""
        # Retrieve default settings in case user don't override them.
        default_x_size, default_y_size = PuzzleGameSettings.get_default_board_size()
        default_difficulty = PuzzleGameSettings.get_default_difficulty()

        # Smart update only those variables which is None
        if not x_size:
            x_size = default_x_size
        if not y_size:
            y_size = default_y_size
        if not difficulty:
            difficulty = default_difficulty

        # Create a bord and proceed with valid random shuffling.
        board = PuzzleBoard()
        board.valid_random_shuffle(difficulty=difficulty, x_size=x_size, y_size=y_size)
        self.board = board

    def _game_frame_view(self):
        """Prints current game state."""
        # clear and update tabulate view. OS independent approach
        # for windows
        if os.name == 'nt':
            os.system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            os.system('clear')
        self.board.board_view()