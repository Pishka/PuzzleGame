from attr import dataclass
from dynaconf import settings
from typing import Tuple, Type

from game.core.utils.puzzle_dificulty_enum import PuzzleDifficultyEnum

@dataclass
class PuzzleGameSettings:
    """
    Orchestrator of profile settings.
    Manipulate settings.json to retrieve default Game settings.
    """

    DEFAULT_SOURCES_CONFIG = 'settings.json'
    """Private class attribute to store path from root of project to environment settings."""

    @classmethod
    def get_default_board_size(cls) -> Tuple[int , int]:
        """Returns tuple with default dynaconf size settings."""
        return (settings.DefaultXCoordinateSize, settings.DefaultYCoordinateSize)

    @classmethod
    def get_default_difficulty(cls) -> Type[PuzzleDifficultyEnum]:
        """Return game default difficulty."""
        return PuzzleDifficultyEnum[settings.DefaultDifficulty]