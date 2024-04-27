from __future__ import annotations
from Creatues import Creatues
from Coordinate import Coordinate
from Directions import Direction

class Piece:

    def __init__(self, firstPlayer: bool, creature: Creatues, index: int, coordinate: Coordinate) -> None:
        self.firstPlayer = firstPlayer
        self.creature = creature
        self.index = index
        self.coordinate = coordinate

    def pieceToMove(self, direction: Direction):
        return Piece(self.firstPlayer, self.creature, self.index, self.coordinate.NeighbourCoordinate(direction))

    def sameKind(self, other: Piece):
        return(
            self.firstPlayer == other.firstPlayer and 
            self.creature == other.creature and 
            self.index == other.index)
    
    def print(self) -> str:
        if(self.firstPlayer):
            return self.creature.value.upper() + str(self.index) + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"
        else:
            return self.creature.value.lower() + str(self.index) + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, Piece):
            return self.sameKind(other) and self.coordinate == other.coordinate # type: ignore
        return False