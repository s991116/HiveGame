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

  def Build(self, hivePiece: HivePiece, coordinate:Coordinate) -> BoardPiece:
    (creature, index, firstPlayer) = HivePieceBuilder.HivePiecesDictionary[hivePiece]
    pr = PieceRules()

    if creature == Creatures.Grasshopper:
      pr = PieceRulesGrasshopper()

    if creature == Creatures.QueenBee:
      pr = PieceRulesQueenBee()

    return BoardPiece(Piece(firstPlayer, creature, index), coordinate, pr)