from __future__ import annotations

from typing import TYPE_CHECKING
from app.HivePiece import HivePiece
from app.HiveGame import HiveGame
from app.Coordinate import Coordinate
from app.BoardPieceBuilder import BoardPieceBuilder

if TYPE_CHECKING:
  from app.BoardPiece import BoardPiece


class HiveGameTestBuilder:

  def __init__(self) -> None:
    self.placements: list[BoardPiece] = []
    pass

  def Play(self, hivePiece: HivePiece, x: int,y: int):
    self.placements.append(BoardPieceBuilder().WithHivePiece(hivePiece, Coordinate(x, y)).Build())
    return self

  def Build(self) -> HiveGame:
    hiveGame = HiveGame()
    for boardPiece in self.placements:
      hiveGame.playMove(boardPiece)
    return hiveGame