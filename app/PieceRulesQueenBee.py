from __future__ import annotations
from typing import List
from app.PieceRules import PieceRules
import app.BoardPiece as BP
import app.HiveBoard as HB

class PieceRulesQueenBee(PieceRules):

  def getMoves(self, boardPiece: BP.BoardPiece, board: HB.HiveBoard) -> List[BP.BoardPiece]:
    return []
