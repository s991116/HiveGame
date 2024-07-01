from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
import app.HiveBoard as HB

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece

class PieceRulesBeetle(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    moves = super().moveAlongPieces(boardPiece, board, 1)
    return moves
