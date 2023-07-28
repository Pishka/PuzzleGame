from enum import Enum


class PuzzleValidMovesEnum(Enum):
    """System available moves for user."""

    q = 0
    """Quit from the game."""

    w = 1
    """Go up."""

    a = 2
    """Go down."""

    d = 3
    """Go left."""

    s = 4
    """Go right."""