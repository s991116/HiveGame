from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
from app.Directions import Direction
import app.BoardPieceBuilder as HP

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.HiveBoard import HiveBoard


class PieceRulesGrasshopper(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:

    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    moves: List[BoardPiece] = []
    for direction in directions:
      directionCoordinate = boardPiece.coordinate
      piecePresent = True
      distance = 0
      while piecePresent:
        directionCoordinate = board.navigate(direction, directionCoordinate)
        piecePresent = not board.isPlaceFree(directionCoordinate)
        distance += 1
      if distance > 1:
        move = HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(directionCoordinate).Build()
        moves.append(move)

    return moves
