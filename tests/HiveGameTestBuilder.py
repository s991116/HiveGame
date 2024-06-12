from __future__ import annotations

from app.HivePiece import HivePiece
from app.HivePieces import HivePieces
from app.HiveGame import HiveGame
from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece

class HiveGameTestBuilder:

  def __init__(self) -> None:
    self.hivePieces = HivePieces()
    self.placements: list[BoardPiece] = []
    pass

  def Play(self, hivePiece: HivePiece, x: int,y: int):
    self.placements.append(HivePieces.CreateBoardPiece2(hivePiece,Coordinate(x, y)))
    return self

  def Build(self) -> HiveGame:
    hiveGame = HiveGame()
    for boardPiece in self.placements:
      hiveGame.playMove(boardPiece)
    return hiveGame