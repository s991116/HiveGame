from dataclasses import dataclass

@dataclass
class Piece:
    firstPlayer: bool
    type: int
    index: int

@dataclass
class Position:
    x: int
    y: int
