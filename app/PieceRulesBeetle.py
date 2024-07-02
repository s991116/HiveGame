from __future__ import annotations

from typing import List, TYPE_CHECKING
from app.PieceRules import PieceRules
from app.Directions import Direction
import app.HiveBoard as HB
import app.BoardPieceBuilder as HP


if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece
  from app.Coordinate import Coordinate

class PieceRulesBeetle(PieceRules):

  def getMoves(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    movesAlongEdge = super().moveAlongPieces(boardPiece, board, 1)

    movesOnTop = self.moveOnTop(boardPiece, board)

    return movesAlongEdge + movesOnTop

  def moveOnTop(self, boardPiece: BoardPiece, board: HB.HiveBoard) -> List[BoardPiece]:
    coordinates = self.findNonEmptyNeightbourCoordinates(boardPiece, board)
    moves: List[BoardPiece] = []
    for (coordinate, layer) in coordinates:
      #board.getBoardPiece(coordinate)
      move = HP.BoardPieceBuilder().WithPiece(boardPiece.piece).WithCoordinate(coordinate).Layer(layer+1).Build()
      moves.append(move)

    return moves
  
  def findNonEmptyNeightbourCoordinates(self,  boardPiece: BoardPiece, board: HB.HiveBoard) -> list[tuple[Coordinate, int]]:
    upDownCoordinates: list[tuple[Coordinate, int]] = []
    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]
    for direction in directions:
      neighboardCoordinate = board.navigate(direction, boardPiece.coordinate)
      boardLayer = board.getLayer(neighboardCoordinate)
      if boardLayer > -1:
        upDownCoordinates.append((neighboardCoordinate, boardPiece.layer))
    return upDownCoordinates

