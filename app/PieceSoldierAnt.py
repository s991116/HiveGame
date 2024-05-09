from typing import List
from app.BoardPiece import BoardPiece
from app.Creatures import Creatures
from app.Coordinate import Coordinate
from app.Piece import Piece

class PieceSoldierAnt(BoardPiece):
  
  def __init__(self, firstPlayer:bool, index: int, coordinate: Coordinate) -> None:
    super().__init__(Piece(firstPlayer, Creatures.SoldierAnt, index), coordinate)

  def getMoves(self, board: List[BoardPiece]) -> List[BoardPiece]:
    return []
