from __future__ import annotations
from typing import List
from app.Coordinate import Coordinate
from app.Directions import Direction
from app.Piece import Piece

class BoardPiece:

    def __init__(self, piece: Piece, coordinate: Coordinate) -> None:
        self.piece = piece
        self.coordinate = coordinate

    def pieceToMove(self, direction: Direction):
        return BoardPiece(self.piece, self.coordinate.NeighbourCoordinate(direction))
    
    def samePiece(self, piece: Piece) -> List[BoardPiece]:
        if(piece == self.piece):
            return [self]
        else:
            return []

    def print(self) -> str:
        return self.piece.print() + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, BoardPiece):
            return self.piece == other.piece and self.coordinate == other.coordinate
        return False