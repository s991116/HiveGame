from typing import List, Tuple
from Piece import Piece, Position


class HiveGame:

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
        moves.append((piece, self.centerPosition))

    return moves
    
  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self._board
  