import pytest

from game.core.puzzle_board import PuzzleBoard
from game.core.utils.puzzle_point_coordinate import PuzzlePoint
from game.core.utils.puzzle_valid_moves_enum import PuzzleValidMovesEnum


class TestPuzzleBoard:

    def test_board_solved(self):
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
        assert board.board_solved() is True
        # Invalid board testing
        invalid_board_data = [
            [1, 2 , 3],
            [4 , 5 , 6],
            [7, board.empty_square, 8],
        ]
        board.data = invalid_board_data
        assert board.board_solved() is False

    def test_board_view(self):
        # Init setup for board
        x_size = 3
        y_size = 3
        empty_point = PuzzlePoint(x=2, y=2)
        board = PuzzleBoard(empty_point=empty_point, x_size=x_size, y_size=y_size)
        board_data = [
            [1, 2 , 3],
            [4 , 5 , 6],
            [7, 8, board.empty_square],
        ]
        board.data = board_data
        before_view = board._board_view()
        board.move(PuzzleValidMovesEnum.w)
        board.move(PuzzleValidMovesEnum.s)
        after_view = board._board_view()

        assert before_view == after_view

    def test_move(self):
        # Init setup for board
        x_size = 3
        y_size = 3
        empty_point = PuzzlePoint(x=1, y=1)
        board = PuzzleBoard(empty_point=empty_point, x_size=x_size, y_size=y_size)
        board_data = [
            [1, 2 , 3],
            [4 , board.empty_square , 6],
            [7, 8, 5],
        ]
        board.data = board_data
        # scope of expectations
        expected_w_board_data = [
            [1, board.empty_square , 3],
            [4 , 2 , 6],
            [7, 8, 5],
        ]
        expected_d_board_data = [
            [1, 3 , board.empty_square],
            [4 , 2 , 6],
            [7, 8, 5],
        ]
        expected_s_board_data = [
            [1, 3 , 6],
            [4 , 2 , board.empty_square],
            [7, 8, 5],
        ]
        expected_a_board_data = board_data
        # results review
        board.move(PuzzleValidMovesEnum.w)
        assert board.data == expected_w_board_data
        board.move(PuzzleValidMovesEnum.d)
        assert board.data == expected_d_board_data
        board.move(PuzzleValidMovesEnum.s)
        assert board.data == expected_s_board_data
        board.move(PuzzleValidMovesEnum.a)
        assert board.data == expected_a_board_data

    def test_move_complex(self):
        """Complex test for move."""
        # Init setup for board
        x_size = 3
        y_size = 3
        empty_point = PuzzlePoint(x=1, y=1)
        board = PuzzleBoard(empty_point=empty_point, x_size=x_size, y_size=y_size)
        board_data = [
            [1, 2 , 3],
            [4 , board.empty_square , 6],
            [7, 8, 5],
        ]
        board.data = board_data

        expected_result = board_data.copy()

        board.move(PuzzleValidMovesEnum.w)
        board.move(PuzzleValidMovesEnum.s)
        board.move(PuzzleValidMovesEnum.w)
        board.move(PuzzleValidMovesEnum.s)
        assert board.data == expected_result

        board.move(PuzzleValidMovesEnum.a)
        board.move(PuzzleValidMovesEnum.d)
        board.move(PuzzleValidMovesEnum.a)
        board.move(PuzzleValidMovesEnum.d)
        assert board.data == expected_result


if __name__ == '__main__':
    pytest.main([__file__])
