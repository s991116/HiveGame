from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
import app.HiveBoard as HB
import app.BoardPieceBuilder as HP

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece

class PieceRulesAnt(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    
    moves : List[BoardPiece] = []
    searchCoordinate = boardPiece.coordinate
    while True:
      moveToAdd  = super().findNextStep([searchCoordinate], boardPiece.coordinate, True, board)

      if not moveToAdd or boardPiece.coordinate == moveToAdd[0]:
        break
      else:
        searchCoordinate = moveToAdd[0]
        moves.append(HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(moveToAdd[0]).Build())

    return moves
