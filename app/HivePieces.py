from __future__ import annotations

from typing import List, Optional, Dict
from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatures import Creatures

from app.PieceRules import PieceRules
from app.PieceRulesGrasshopper import PieceRulesGrasshopper
from app.PieceRulesQueenBee import PieceRulesQueenBee

from app.HivePiece import HivePiece

class HivePieces:

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
    c = Coordinate(0,0)
    self.QueenBee_P1       = HivePieces.CreateBoardPiece(True, Creatures.QueenBee, 0, c)
    self.Grasshopper_0_P1 = HivePieces.CreateBoardPiece(True, Creatures.Grasshopper, 0, c)
    self.Grasshopper_1_P1 = HivePieces.CreateBoardPiece(True, Creatures.Grasshopper, 1, c)
    self.Grasshopper_2_P1 = HivePieces.CreateBoardPiece(True, Creatures.Grasshopper, 2, c)
    self.Spider_0_P1      = HivePieces.CreateBoardPiece(True, Creatures.Spider, 0, c)
    self.Spider_1_P1      = HivePieces.CreateBoardPiece(True, Creatures.Spider, 1, c)
    self.Ant_0_P1         = HivePieces.CreateBoardPiece(True, Creatures.SoldierAnt, 0, c)
    self.Ant_1_P1         = HivePieces.CreateBoardPiece(True, Creatures.SoldierAnt, 1, c)
    self.Ant_2_P1         = HivePieces.CreateBoardPiece(True, Creatures.SoldierAnt, 2, c)
    self.Beetle_0_P1      = HivePieces.CreateBoardPiece(True, Creatures.Beetle, 0, c)
    self.Beetle_1_P1      = HivePieces.CreateBoardPiece(True, Creatures.Beetle, 1, c)

    self.QueenBee_P2      = HivePieces.CreateBoardPiece(False, Creatures.QueenBee, 0, c)
    self.Grasshopper_0_P2 = HivePieces.CreateBoardPiece(False, Creatures.Grasshopper, 0, c)
    self.Grasshopper_1_P2 = HivePieces.CreateBoardPiece(False, Creatures.Grasshopper, 1, c)
    self.Grasshopper_2_P2 = HivePieces.CreateBoardPiece(False, Creatures.Grasshopper, 2, c)
    self.Spider_0_P2      = HivePieces.CreateBoardPiece(False, Creatures.Spider, 0, c)
    self.Spider_1_P2      = HivePieces.CreateBoardPiece(False, Creatures.Spider, 1, c)
    self.Ant_0_P2         = HivePieces.CreateBoardPiece(False, Creatures.SoldierAnt, 0, c)
    self.Ant_1_P2         = HivePieces.CreateBoardPiece(False, Creatures.SoldierAnt, 1, c)
    self.Ant_2_P2         = HivePieces.CreateBoardPiece(False, Creatures.SoldierAnt, 2, c)
    self.Beetle_0_P2      = HivePieces.CreateBoardPiece(False, Creatures.Beetle, 0, c)
    self.Beetle_1_P2      = HivePieces.CreateBoardPiece(False, Creatures.Beetle, 1, c)

    self._freePiecesP1: List[BoardPiece] = [
      self.QueenBee_P1,
      self.Grasshopper_0_P1,
      self.Grasshopper_1_P1,
      self.Grasshopper_2_P1,
      self.Spider_0_P1,
      self.Spider_1_P1,
      self.Ant_0_P1,
      self.Ant_1_P1,
      self.Ant_2_P1,
      self.Beetle_0_P1,
      self.Beetle_1_P1,
    ]

    self._freePiecesP2: List[BoardPiece] = [
      self.QueenBee_P2,
      self.Grasshopper_0_P2,
      self.Grasshopper_1_P2,
      self.Grasshopper_2_P2,
      self.Spider_0_P2,
      self.Spider_1_P2,
      self.Ant_0_P2,
      self.Ant_1_P2,
      self.Ant_2_P2,
      self.Beetle_0_P2,
      self.Beetle_1_P2,
    ]

  @staticmethod
  def CreateBoardPiece(firstPlayer: bool, creature: Creatures, index: int, coordinate: Coordinate) -> BoardPiece:    
    pr = PieceRules()

    if creature == Creatures.Grasshopper:
      pr = PieceRulesGrasshopper()

    if creature == Creatures.QueenBee:
      pr = PieceRulesQueenBee()


    return BoardPiece(Piece(firstPlayer, creature, index), coordinate, pr)

  @staticmethod
  def CreateCloneWithCoordinate(boardPiece: BoardPiece, coordinate: Coordinate) -> BoardPiece:
    return HivePieces.CreateBoardPiece(boardPiece.piece.firstPlayer, boardPiece.piece.creature, boardPiece.piece.index, coordinate)

  def playableFreePieces(self, playerOne:bool):
    playableCreatures: List[BoardPiece] = []

    if playerOne:
      freePieces = self._freePiecesP1
    else:
      freePieces = self._freePiecesP2
    
    for boardPiece in freePieces:
      foundPiece = False
      for playableCreature in playableCreatures:
        if(playableCreature.piece.creature == boardPiece.piece.creature):
          foundPiece = True
          break

      if(not foundPiece):
        playableCreatures.append(boardPiece)

    return playableCreatures

  def removeFromFreePieces(self, boardPiece: BoardPiece) -> None:
      freeBoardPiece = self.findFreePiece(boardPiece)
      if freeBoardPiece is not None:
        if(freeBoardPiece.piece.firstPlayer):
          self._freePiecesP1.remove(freeBoardPiece)
        else:
          self._freePiecesP2.remove(freeBoardPiece)

  def findFreePiece(self, boardPiece: BoardPiece) -> Optional[BoardPiece]:
      if(boardPiece.piece.firstPlayer):
        for freeBoardPiece in self._freePiecesP1:
          if(boardPiece.piece == freeBoardPiece.piece):
            return freeBoardPiece
        return None
      else:
        for freeBoardPiece in self._freePiecesP2:
          if(boardPiece.piece == freeBoardPiece.piece):
            return freeBoardPiece
        return None