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
      nextSteps = [boardPiece.coordinate]
      for _ in range(movesteps):
        nextSteps = self.findNextStep(nextSteps, boardPiece.coordinate, searchDirection, board)
        if not nextSteps:
          break
        else:
          steps += 1

      if(steps == movesteps and nextSteps):
        for nextStep in nextSteps:
          move = HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(nextStep).Build()
          self.addMove(moves, move, boardPiece.coordinate)
    return moves
  
  def findNextStep(self, stepCoordinates: List[Coordinate], startCoordinate: Coordinate, clockwise: bool, board: HiveBoard):
    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    nextMoveCoordinates: List[Coordinate] = []
    rangeIndex = range(6)
    if not clockwise:
      rangeIndex = rangeIndex[::-1]      

    for pieceCoordinate in stepCoordinates:
      for index in range(6):
        #Search for Connected - Free - Free
        connectedDirectionIndex = rangeIndex[index]
        freeMoveDirectionIndex = rangeIndex[(index + 1) % 6]
        freeSpaceDirectionIndex = rangeIndex[(index + 2) % 6]

        #Check if connection with other piece
        #startCoordinate
        connectedCoordinate = board.navigate(directions[connectedDirectionIndex], pieceCoordinate)
        freeMoveCoordinate = board.navigate(directions[freeMoveDirectionIndex], pieceCoordinate)
        freeSpaceCoordinate = board.navigate(directions[freeSpaceDirectionIndex], pieceCoordinate)

        connectedPlace = not board.isPlaceFree(connectedCoordinate) and connectedCoordinate != startCoordinate
        freeMovePlace = board.isPlaceFree(freeMoveCoordinate) or freeMoveCoordinate == startCoordinate
        freeSpacePlace = board.isPlaceFree(freeSpaceCoordinate) or freeSpaceCoordinate == startCoordinate

        if(connectedPlace and freeMovePlace and freeSpacePlace):
          nextMoveCoordinates.append(freeMoveCoordinate)

    return nextMoveCoordinates

  def addMove(self, moves: List[BoardPiece], move: BoardPiece, pieceStartCoordinate: Coordinate):
    if move.coordinate != pieceStartCoordinate:
      moves.append(move)
    return moves
  