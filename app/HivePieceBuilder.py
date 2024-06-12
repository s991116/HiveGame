from __future__ import annotations

from typing import Dict
from app.Creatures import Creatures
from app.HivePiece import HivePiece
from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece
from app.Piece import Piece

from app.PieceRules import PieceRules
from app.PieceRulesGrasshopper import PieceRulesGrasshopper
from app.PieceRulesQueenBee import PieceRulesQueenBee

class HivePieceBuilder:
  
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
    self._creature = Creatures.Grasshopper
    self._index = 0
    self._firstPlayer = True
    self._coordinate = Coordinate(0,0)
    self._pr = PieceRules()

  def Piece(self, hivePiece: HivePiece, coordinate:Coordinate) -> HivePieceBuilder:
    (self._creature, self._index, self._firstPlayer) = HivePieceBuilder.HivePiecesDictionary[hivePiece]
    self._coordinate = coordinate
    
    self._pr = PieceRules()

    if self._creature == Creatures.Grasshopper:
      self._pr = PieceRulesGrasshopper()

    if self._creature == Creatures.QueenBee:
      self._pr = PieceRulesQueenBee()

    return self

  def Creature(self, creature: Creatures):
    self._creature = creature
    return self
  
  def FirstPlayer(self, firstPlayer:bool):
    self._firstPlayer = firstPlayer
    return self

  def Index(self, index: int):
    self._index = index
    return self
  
  def Coordinate(self, coordinate: Coordinate):
    self._coordinate = coordinate
    return self

  def Build(self):
    return BoardPiece(Piece(self._firstPlayer, self._creature, self._index), self._coordinate, self._pr)