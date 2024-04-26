from __future__ import annotations
from Creatues import Creatues
from Coordinate import Coordinate

class Piece:

    def __init__(self, firstPlayer: bool, creature: Creatues, index: int, coordinate: Coordinate) -> None:
        self.firstPlayer = firstPlayer
        self.creature = creature
        self.index = index
        self.coordinate = coordinate

    def sameKind(self, other: Piece):
        return(
            self.firstPlayer == other.firstPlayer and 
            self.creature == other.creature and 
            self.index == other.index)

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, Piece):
            return self.sameKind(other) and self.coordinate == other.coordinate # type: ignore
        return False