from dataclasses import dataclass
from enum import Enum

class Direction(Enum):
    LEFT = "left"
    RIGHT = "right"
    UP_LEFT = "up left"
    DOWN_LEFT = "down left"
    UP_RIGHT = "up right"
    DOWN_RIGHT = "down right"

class Creatues(Enum):
    QueenBee = "queen bee"
    Spider = "spider"
    Beetle = "beetle"
    Grasshopper = "grasshopper"
    SoldierAnt = "soldier ant"
    Mosquity = "mosquito"

@dataclass
class Piece:
    firstPlayer: bool
    type: Creatues
    index: int

@dataclass
class Position:
    x: int
    y: int