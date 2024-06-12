from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
import app.HiveBoard as HB

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece

class PieceRulesAnt(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    return []
