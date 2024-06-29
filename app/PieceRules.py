from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.Directions import Direction
import app.BoardPieceBuilder as HP


if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.HiveBoard import HiveBoard
  from app.Coordinate import Coordinate

class PieceRules:

  def getMoves(self, boardPiece: BoardPiece, board: HiveBoard) -> List[BoardPiece]:
    return []

  def moveAlongPieces(self, boardPiece: BoardPiece, board: HiveBoard, movesteps: int):
    moves: List[BoardPiece] = []
    for searchDirection in [True, False]:
      steps = 0    
      nextStep = boardPiece.coordinate
      for _ in range(movesteps):
        nextStep = self.findNextStep(nextStep, searchDirection, board)
        if nextStep is None:
          break
        else:
          steps += 1

      if(steps == movesteps and nextStep is not None):
        move = HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(nextStep).Build()
        moves.append(move)
    return moves
  
  def findNextStep(self, pieceCoordinate: Coordinate, clockwise: bool, board: HiveBoard):
    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    
    rangeIndex = range(6)
    if not clockwise:
      rangeIndex = rangeIndex[::-1]      

    for index in range(6):
      #Search for Connected - Free - Free
      connectedDirectionIndex = rangeIndex[index]
      freeMoveDirectionIndex = rangeIndex[(index + 1) % 6]
      freeDirectionIndex = rangeIndex[(index + 2) % 6]

      #Check if connection with other piece
      connectedPlace = not board.isPlaceFree(board.navigate(directions[connectedDirectionIndex], pieceCoordinate))
      nextMoveCoordinte = board.navigate(directions[freeMoveDirectionIndex], pieceCoordinate)
      movePlace = board.isPlaceFree(nextMoveCoordinte)
      freePlace = board.isPlaceFree(board.navigate(directions[freeDirectionIndex], pieceCoordinate))

      if(connectedPlace and movePlace and freePlace):
        return nextMoveCoordinte

    return None

  