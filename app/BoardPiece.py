from __future__ import annotations
from typing import List
from app.Coordinate import Coordinate
from app.Piece import Piece
from app.PieceRules import PieceRules

import app.HiveBoard as HB

class BoardPiece:

    def __init__(self, piece: Piece, coordinate: Coordinate, rules: PieceRules) -> None:
        self.piece = piece
        self.coordinate = coordinate
        self.rules = rules

    def getMoves(self, hiveBoard: HB.HiveBoard) -> List[BoardPiece]:
        return self.rules.getMoves(self, hiveBoard)

    def print(self) -> str:
        return self.piece.print() + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, BoardPiece):
            return self.piece == other.piece and self.coordinate == other.coordinate
        return False