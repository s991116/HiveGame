from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules


if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.HiveBoard import HiveBoard

class PieceRulesQueenBee(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:
    
    moves = super().moveAlongPieces(boardPiece, board, 1)
    return moves