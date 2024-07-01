from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.Coordinate import Coordinate
from app.Piece import Piece

if TYPE_CHECKING:
    from app.PieceRules import PieceRules
    from app.HiveBoard import HiveBoard

class BoardPiece:

    def __init__(self, piece: Piece, coordinate: Coordinate, rules: PieceRules, layer: int) -> None:
        self.piece = piece
        self.coordinate = coordinate
        self.rules = rules
        self.layer = layer

    def getMoves(self, hiveBoard: HiveBoard) -> List[BoardPiece]:
        return self.rules.getMoves(self, hiveBoard)

    def print(self) -> str:
        return self.piece.print() + "(" + str(self.coordinate.x) + "," + str(self.coordinate.y) + ")"

    def __eq__(self, other: any): # type: ignore
        if isinstance(other, BoardPiece):
            return self.piece == other.piece and self.coordinate == other.coordinate and self.layer == other.layer
        return False