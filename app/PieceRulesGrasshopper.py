from __future__ import annotations
from typing import List
from app.PieceRules import PieceRules
from app.Coordinate import Coordinate
from app.Directions import Direction
import app.BoardPiece as BP
import app.HiveBoard as HB
import app.HivePieces as HP

class PieceRulesGrasshopper(PieceRules):

  def getMoves(self, boardPiece: BP.BoardPiece, board: HB.HiveBoard) -> List[BP.BoardPiece]:

    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    moves: List[BP.BoardPiece] = []
    for direction in directions:
      directionCoordinate = boardPiece.coordinate
      piecePresent = True
      distance = 0
      while piecePresent:
        directionCoordinate = board.navigate(direction, directionCoordinate)
        piecePresent = not board.isPlaceFree(directionCoordinate)
        distance += 1
      if distance > 1:
        move = HP.HivePieces.CreateCloneWithCoordinate(boardPiece, directionCoordinate)
        moves.append(move)

    return moves
