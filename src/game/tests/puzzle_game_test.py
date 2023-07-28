import pytest

from game.core.puzzle_board import PuzzleBoard
from game.core.puzzle_game import PuzzleGame
from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum
from game.core.utils.puzzle_point_coordinate import PuzzlePoint


class TestPuzzleGame:

    def test_start_game(self):
        # game init
        game = PuzzleGame()
        y_size = 3
        x_size = 3
        # board init
        game._start_game(x_size=3, y_size=3, difficulty=PuzzleDifficultyEnum.Hard)
        game._game_frame_view()

        assert game.board.y_size == y_size
        assert game.board.x_size == x_size

    def test_finished(self):
        # Init setup for game
        game = PuzzleGame()
        # Init setup for board
        x_size = 3
        y_size = 3
        empty_point = PuzzlePoint(x=2, y=2)
        board = PuzzleBoard(empty_point=empty_point, x_size=x_size, y_size=y_size)
        # Valid board testing
        valid_board_data = [
            [1, 2 , 3],
            [4 , 5 , 6],
            [7, 8, board.empty_square],
        ]
        board.data = valid_board_data
        game.board = board
        assert game.is_game_finished() is True
        # Invalid board testing
        invalid_board_data = [
            [1, 2 , 3],
            [4 , 5 , 6],
            [7, board.empty_square, 8],
        ]
        board.data = invalid_board_data
        assert game.is_game_finished() is False


if __name__ == '__main__':
    pytest.main([__file__])
