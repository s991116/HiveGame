from typing import List, Tuple
from Piece import Piece, Position


class HiveGame:

  def __init__(self) -> None:
    self.playerOnePieces = [Piece(True,1,0), Piece(True,2,0), Piece(True,3,0), Piece(True,4,0), Piece(True,5,0)]
    self.playerTwoPieces = [Piece(False,1,0), Piece(False,2,0), Piece(False,3,0), Piece(False,4,0), Piece(False,5,0)]
    self.centerPosition = (0,0)
    self._board = []

  def setPiece(self, piece: Piece, position: Position):
    self._board.append((piece, position))

  def getValidMoves(self):
    moves = []
    for piece in self.playerOnePieces:
      moves.append((piece, self.centerPosition))
    return moves
    
  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self._board
  