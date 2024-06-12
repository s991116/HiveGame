from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
from app.Directions import Direction

import app.BoardPieceBuilder as HP

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.HiveBoard import HiveBoard

class PieceRulesQueenBee(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:

    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    moves: List[BoardPiece] = []
    queenCoordinate = boardPiece.coordinate

    for index, direction in enumerate(directions):
      #Check if connection with other piece
      directionCoordinate = board.navigate(direction, queenCoordinate)
      pieceConnected = not board.isPlaceFree(directionCoordinate)      

      #Check if movement clockwise and anti-clockwise is possible
      for clockwiseStep in [-1, 1]:
        if pieceConnected:
          directionClockwise = directions[(index+clockwiseStep) % 6]
          coordinateClockwise = board.navigate(directionClockwise, queenCoordinate)
          clockwiseFree = board.isPlaceFree(coordinateClockwise)
          if clockwiseFree:
            #Check if space available to move
            direction2xClockwise = directions[(index+2*clockwiseStep) % 6]
            clockwise2xFree = board.isPlaceFree(board.navigate(direction2xClockwise, queenCoordinate))

            if clockwise2xFree:
              move = HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(coordinateClockwise).Build()
              moves.append(move)

    return moves