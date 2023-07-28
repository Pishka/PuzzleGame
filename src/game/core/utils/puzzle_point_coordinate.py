import attr
from attr import dataclass


@dataclass
class PuzzlePoint:
    """Data class to store information about x and y coordinate of point in Board."""

    x: int = attr.ib(default=0, kw_only=True)
    """X coordinate of puzzle point."""

    y: int = attr.ib(default=0, kw_only=True)
    """Y coordinate of puzzle point."""