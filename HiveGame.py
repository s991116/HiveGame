from typing import List, Tuple, Dict
from Piece import Piece, Position

from enum import Enum

class Direction(Enum):
  LEFT = "left"
  RIGHT = "right"
  UP_LEFT = "up left"
  DOWN_LEFT = "down left"
  UP_RIGHT = "up right"
  DOWN_RIGHT = "down right"


class HiveGame:

  _directionVector: Dict[Direction, Tuple[int,int]] = {
     Direction.LEFT:       (-1, 0),
     Direction.RIGHT:      ( 1, 0),
     Direction.UP_LEFT:    ( 1, 1),
     Direction.UP_RIGHT:   ( 0, 1),
     Direction.DOWN_LEFT:  (-1,-1),
     Direction.DOWN_RIGHT: ( 0,-1)}

  def __init__(self) -> None:
    self.playerOnePieces: list[Piece] = [Piece(True,1,0), Piece(True,2,0), Piece(True,3,0), Piece(True,4,0), Piece(True,5,0)]
    self.playerTwoPieces: list[Piece] = [Piece(False,1,0), Piece(False,2,0), Piece(False,3,0), Piece(False,4,0), Piece(False,5,0)]
    self.centerPosition: Position = Position(0,0)
    self._board: list[Tuple[Piece, Position]] = []
    self._playerOneTurns = True

  def setPiece(self, move: Tuple[Piece, Position]):
    self._playerOneTurns = not self._playerOneTurns
    self._board.append(move)

  def getValidMoves(self) -> List[Tuple[Piece, Position]]:
    moves:list[Tuple[Piece, Position]] = []
    if(self._playerOneTurns):
      for piece in self.playerOnePieces:
        moves.append((piece, self.centerPosition))
    else:
      for piece in self.playerTwoPieces:
        moves.append((piece, self._navigate(Direction.LEFT, self.centerPosition)))

    return moves
  
  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self._board
  
  def moveLeft(self) -> None:
    self.x = self.x-1

  def _navigate(self, direction: Direction, position: Position) -> Position:
    (xstep, ystep) = self._directionVector[direction]
    return Position(position.x+xstep, position.y+ystep)
