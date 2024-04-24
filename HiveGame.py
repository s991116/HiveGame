from typing import List, Tuple
from Piece import Piece, Position


class HiveGame:

  def __init__(self) -> None:
    self.playerOnePieces = [Piece(True,1,0)]
    self.playerTwoPieces = [Piece(False,1,0)]
    self.centerPosition = (0,0)
    self._board = []

  def SetPiece(self, piece: Piece, position: Position):
    self._board.append((piece, position))
    
  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self._board
  