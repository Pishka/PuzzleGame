from typing import List, Type, Any, Optional

import tabulate
import attr
import random
from attr import dataclass

from game.core.utils.puzzle_valid_moves_enum import PuzzleValidMovesEnum
from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum
from game.core.utils.puzzle_point_coordinate import PuzzlePoint


@dataclass
class PuzzleBoard:
    """Class which represents API to manipulate game board."""

    empty_point: PuzzlePoint = attr.ib(default=None, kw_only=True)
    """Information about *(empty) square in the game"""

    data: List[List[Any]] = attr.ib(default=None, kw_only=True)
    """Current board state."""

    x_size: int = attr.ib(default=None, kw_only=True)
    """X dimension size of board."""

    y_size: int = attr.ib(default=None, kw_only=True)
    """Y dimension size of board."""

    empty_square: Optional[str] = attr.ib(default='*', kw_only=True)
    """Symbol that indicates empty square."""

    def board_solved(self) -> bool:
        """Return True if game is solved and finished."""
        num = 1
        for i in range(self.x_size):
            for j in range(self.y_size):
                # Indicates the end of board
                if i == self.x_size - 1 and j == self.y_size - 1:
                    # return true only in case end square is empty square
                    return self.data[i][j] == self.empty_square
                # If we meet __empty_square inside or value not correct -> return False
                if isinstance(self.data[i][j], str) or self.data[i][j] != num:
                    return False
                num += 1
        return True

    def board_view(self):
        """Prints current state of board tabulated values."""
        print(self._board_view())

    def valid_random_shuffle(self, difficulty: PuzzleDifficultyEnum, x_size: int, y_size: int):
        """Creates based on game size and difficulty valid data shuffle."""
        result: List[List[Any]] = []
        num = 1
        # Generating end position and empty point.
        for i in range(x_size):
            row = []
            for _ in range(y_size):
                row.append(num)
                num += 1
            result.append(row)
        result[x_size-1][y_size-1] = self.empty_square
        self.data = result
        # Empty point setting
        self.empty_point = PuzzlePoint(x=x_size-1, y=y_size-1)
        self.x_size = x_size
        self.y_size = y_size
        # Backward shuffling.
        max_num_of_shuffles = difficulty.value
        num_of_shuffles = random.randint(0, max_num_of_shuffles)
        # Possible directions
        possible_directions = [e.name for e in PuzzleValidMovesEnum]
        for _ in range(num_of_shuffles):
            int_direction = random.randint(1, 4)
            # getting random moving direction
            direction = PuzzleValidMovesEnum[possible_directions[int_direction]]
            # Making only possible backward moves
            try:
                self.move(direction=direction)
            finally:
                continue

    def move(self, direction: Type[PuzzleValidMovesEnum]):
        """Factory unified method to proceed with moving."""
        if direction == PuzzleValidMovesEnum.w:
            swap_x, swap_y = self.empty_point.x - 1, self.empty_point.y
        elif direction == PuzzleValidMovesEnum.a:
            swap_x, swap_y = self.empty_point.x, self.empty_point.y - 1
        elif direction == PuzzleValidMovesEnum.s:
            swap_x, swap_y = self.empty_point.x + 1, self.empty_point.y
        elif direction == PuzzleValidMovesEnum.d:
            swap_x, swap_y = self.empty_point.x, self.empty_point.y + 1
        else:
            raise NotImplementedError(f"{PuzzleValidMovesEnum.s} move is not acceptable for system.")
        self._move(swap_x=swap_x, swap_y=swap_y)

    def _move(self, swap_x: int, swap_y: int):
        """Unified method to proceed with moving of empty square."""
        if swap_x < 0 or swap_y < 0:
            raise IndexError(f"Out of board border. Expected value >= 0 get < 0 instead")
        self.data[self.empty_point.x][self.empty_point.y], self.data[swap_x][swap_y] = self.data[swap_x][swap_y], \
                                                                                       self.data[self.empty_point.x][
                                                                                           self.empty_point.y]
        self.empty_point.x = swap_x
        self.empty_point.y = swap_y

    def _board_view(self) -> str:
        """Return current state of board tabulated values as string."""
        return tabulate.tabulate(self.data)
