from __future__ import annotations

from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP_LEFT = "up left"
    DOWN_LEFT = "down left"
    UP_RIGHT = "up right"
    DOWN_RIGHT = "down right"

class Directions:
    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]