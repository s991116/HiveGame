from __future__ import annotations

from typing import Dict

from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatures import Creatures

from app.PieceRules import PieceRules
from app.PieceRulesGrasshopper import PieceRulesGrasshopper
from app.PieceRulesQueenBee import PieceRulesQueenBee
from app.HivePiece import HivePiece
from app. PieceBuilder import PieceBuilder

class BoardPieceBuilder:

  HivePiecesDictionary: Dict[HivePiece, tuple[Creatures, int, bool]] = {
    HivePiece.QueenBee_P1: (Creatures.QueenBee, 0, True),
    HivePiece.QueenBee_P2: (Creatures.QueenBee, 0, False),

    HivePiece.Beetle_0_P1: (Creatures.Beetle, 0, True),
    HivePiece.Beetle_1_P1: (Creatures.Beetle, 1, True),
    HivePiece.Beetle_0_P2: (Creatures.Beetle, 0, False),
    HivePiece.Beetle_1_P2: (Creatures.Beetle, 1, False),

    HivePiece.Grasshopper_0_P1: (Creatures.Grasshopper, 0, True),
    HivePiece.Grasshopper_1_P1: (Creatures.Grasshopper, 1, True),
    HivePiece.Grasshopper_2_P1: (Creatures.Grasshopper, 2, True),
    HivePiece.Grasshopper_0_P2: (Creatures.Grasshopper, 0, False),
    HivePiece.Grasshopper_1_P2: (Creatures.Grasshopper, 1, False),
    HivePiece.Grasshopper_2_P2: (Creatures.Grasshopper, 2, False),

    HivePiece.SoldierAnt_0_P1: (Creatures.SoldierAnt, 0, True),
    HivePiece.SoldierAnt_1_P1: (Creatures.SoldierAnt, 1, True),
    HivePiece.SoldierAnt_2_P1: (Creatures.SoldierAnt, 2, True),
    HivePiece.SoldierAnt_0_P2: (Creatures.SoldierAnt, 0, False),
    HivePiece.SoldierAnt_1_P2: (Creatures.SoldierAnt, 1, False),
    HivePiece.SoldierAnt_2_P2: (Creatures.SoldierAnt, 2, False),

    HivePiece.Spider_0_P1: (Creatures.Spider, 0, True),
    HivePiece.Spider_1_P1: (Creatures.Spider, 1, True),
    HivePiece.Spider_0_P2: (Creatures.Spider, 0, False),
    HivePiece.Spider_1_P2: (Creatures.Spider, 1, False),
  }

  def __init__(self) -> None:
    self._coordinate = Coordinate(0,0)
    self._pr = PieceRules()
    self._piece = PieceBuilder().Build()

  def updateRules(self, creature: Creatures):
    self._pr = PieceRules()

    if creature == Creatures.Grasshopper:
      self._pr = PieceRulesGrasshopper()

    if creature == Creatures.QueenBee:
      self._pr = PieceRulesQueenBee()

  def WithPiece(self, piece: Piece):
    self._piece = piece
    self.updateRules(piece.creature)
    return self

  def WithHivePiece(self, hivePiece: HivePiece, coordinate: Coordinate) -> BoardPieceBuilder:
    (creature, index, firstPlayer) = BoardPieceBuilder.HivePiecesDictionary[hivePiece]
    self._piece = PieceBuilder().With(creature, index, firstPlayer).Build()
    self.updateRules(creature)
    self.WithCoordinate(coordinate)
    return self

  def WithCoordinate(self, coordinate: Coordinate):
    self._coordinate = coordinate
    return self

  def Build(self):
    return BoardPiece(self._piece, self._coordinate, self._pr)