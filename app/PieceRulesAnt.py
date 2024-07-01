from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
import app.HiveBoard as HB
import app.BoardPieceBuilder as HP

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.Coordinate import Coordinate

class PieceRulesAnt(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    
    moveCoordinates : List[Coordinate] = []
    
    for clockwise in [True, False]:
      searchCoordinate = boardPiece.coordinate
      while True:
        moveToAdd  = super().findNextStep([searchCoordinate], boardPiece.coordinate, clockwise, board)

        if not moveToAdd or boardPiece.coordinate == moveToAdd[0]:
          break
        else:
          searchCoordinate = moveToAdd[0]
          if searchCoordinate not in moveCoordinates:
            moveCoordinates.append(searchCoordinate)

    moves : List[BoardPiece] = []
    for moveCoordinate in moveCoordinates:
      moves.append(HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(moveCoordinate).Build())
    return moves
