from __future__ import annotations

from typing import Dict

from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Species import Species

from app.PieceRules import PieceRules
from app.PieceRulesGrasshopper import PieceRulesGrasshopper
from app.PieceRulesQueenBee import PieceRulesQueenBee
from app.PieceRulesSpider import PieceRulesSpider
from app.PieceRulesAnt import PieceRulesAnt
from app.PieceRulesBeetle import PieceRulesBeetle

from app.HivePiece import HivePiece
from app. PieceBuilder import PieceBuilder

class BoardPieceBuilder:

  HivePiecesDictionary: Dict[HivePiece, tuple[Species, int, bool]] = {
    HivePiece.QueenBee_P1: (Species.QueenBee, 0, True),
    HivePiece.QueenBee_P2: (Species.QueenBee, 0, False),

    HivePiece.Beetle_0_P1: (Species.Beetle, 0, True),
    HivePiece.Beetle_1_P1: (Species.Beetle, 1, True),
    HivePiece.Beetle_0_P2: (Species.Beetle, 0, False),
    HivePiece.Beetle_1_P2: (Species.Beetle, 1, False),

    HivePiece.Grasshopper_0_P1: (Species.Grasshopper, 0, True),
    HivePiece.Grasshopper_1_P1: (Species.Grasshopper, 1, True),
    HivePiece.Grasshopper_2_P1: (Species.Grasshopper, 2, True),
    HivePiece.Grasshopper_0_P2: (Species.Grasshopper, 0, False),
    HivePiece.Grasshopper_1_P2: (Species.Grasshopper, 1, False),
    HivePiece.Grasshopper_2_P2: (Species.Grasshopper, 2, False),

    HivePiece.Ant_0_P1: (Species.Ant, 0, True),
    HivePiece.Ant_1_P1: (Species.Ant, 1, True),
    HivePiece.Ant_2_P1: (Species.Ant, 2, True),
    HivePiece.Ant_0_P2: (Species.Ant, 0, False),
    HivePiece.Ant_1_P2: (Species.Ant, 1, False),
    HivePiece.Ant_2_P2: (Species.Ant, 2, False),

    HivePiece.Spider_0_P1: (Species.Spider, 0, True),
    HivePiece.Spider_1_P1: (Species.Spider, 1, True),
    HivePiece.Spider_0_P2: (Species.Spider, 0, False),
    HivePiece.Spider_1_P2: (Species.Spider, 1, False),
  }

  def __init__(self) -> None:
    self._coordinate = Coordinate(0,0)
    self._pr = PieceRules()
    self._piece = PieceBuilder().Build()
    self._layer = 0

  def updateRules(self, creature: Species):
    self._pr = PieceRules()

    if creature == Species.Grasshopper:
      self._pr = PieceRulesGrasshopper()

    if creature == Species.Spider:
      self._pr = PieceRulesSpider()

    if creature == Species.QueenBee:
      self._pr = PieceRulesQueenBee()

    if creature == Species.Ant:
      self._pr = PieceRulesAnt()

    if creature == Species.Beetle:
      self._pr = PieceRulesBeetle()


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
  
  def Layer(self, layer:int):
    self._layer = layer
    return self

  def Build(self):
    return BoardPiece(self._piece, self._coordinate, self._pr, self._layer)