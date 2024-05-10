from typing import List
from app.BoardPiece import BoardPiece
from app.HiveBoard import HiveBoard
from app.PieceRules import PieceRules

class PieceRulesBeetle(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:
    return []
