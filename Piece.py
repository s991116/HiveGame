from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP_LEFT = "up left"
    DOWN_LEFT = "down left"
    UP_RIGHT = "up right"
    DOWN_RIGHT = "down right"

@dataclass
class Piece:
    firstPlayer: bool
    type: int
    index: int

@dataclass
class Position:
    x: int
    y: int