from __future__ import annotations
from typing import List
from app.Coordinate import Coordinate
from app.Piece import Piece

class BoardPiece:

    def __init__(self, piece: Piece, coordinate: Coordinate) -> None:
        self.piece = piece
        self.coordinate = coordinate

    def getMoves(self, board: List[BoardPiece]) -> List[BoardPiece]:
        return []

    def print(self) -> str:
        return self.piece.print() + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, BoardPiece):
            return self.piece == other.piece and self.coordinate == other.coordinate
        return False