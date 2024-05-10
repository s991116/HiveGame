from typing import List, Optional
from app.PieceGrasshopper import PieceGrasshopper
from app.Coordinate import Coordinate
from app.PieceQueenBee import PieceQueenBee
from app.PieceSoldierAnt import PieceSoldierAnt
from app.PieceSpider import PieceSpider
from app.PieceBeetle import PieceBeetle
from app.Creatures import Creatures
from app.BoardPiece import BoardPiece

class HivePieces:
  def __init__(self) -> None:
    c = Coordinate(0,0)
    self.QueenBee_P1       =PieceQueenBee(True, 0, c)
    self.Grasshopper_0_P1 = PieceGrasshopper(True, 0, c)
    self.Grasshopper_1_P1 = PieceGrasshopper(True, 1, c)
    self.Grasshopper_2_P1 = PieceGrasshopper(True, 2, c)
    self.Spider_0_P1      = PieceSpider(True, 0, c)
    self.Spider_1_P1      = PieceSpider(True, 1, c)
    self.Ant_0_P1         = PieceSoldierAnt(True, 0, c)
    self.Ant_1_P1         = PieceSoldierAnt(True, 1, c)
    self.Ant_2_P1         = PieceSoldierAnt(True, 2, c)
    self.Beetle_0_P1      = PieceBeetle(True, 0, c)
    self.Beetle_1_P1      = PieceBeetle(True, 1, c)

    self.QueenBee_P2      = PieceQueenBee(False, 0, c)
    self.Grasshopper_0_P2 = PieceGrasshopper(False, 0, c)
    self.Grasshopper_1_P2 = PieceGrasshopper(False, 1, c)
    self.Grasshopper_2_P2 = PieceGrasshopper(False, 2, c)
    self.Spider_0_P2      = PieceSpider(False, 0, c)
    self.Spider_1_P2      = PieceSpider(False, 1, c)
    self.Ant_0_P2         = PieceSoldierAnt(False, 0, c)
    self.Ant_1_P2         = PieceSoldierAnt(False, 1, c)
    self.Ant_2_P2         = PieceSoldierAnt(False, 2, c)
    self.Beetle_0_P2      = PieceBeetle(False, 0, c)
    self.Beetle_1_P2      = PieceBeetle(False, 1, c)

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
    
    if creature == Creatures.Beetle:
      return PieceBeetle(firstPlayer, index, coordinate)
    if creature == Creatures.Grasshopper:
      return PieceGrasshopper(firstPlayer, index, coordinate)
    if creature == Creatures.SoldierAnt:
      return PieceSoldierAnt(firstPlayer, index, coordinate)
    if creature == Creatures.QueenBee:
      return PieceQueenBee(firstPlayer, index, coordinate)
    if creature == Creatures.Spider:
      return PieceSpider(firstPlayer, index, coordinate)

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
          if(boardPiece == freeBoardPiece):
            return freeBoardPiece
        return None
      else:
        for freeBoardPiece in self._freePiecesP2:
          if(boardPiece == freeBoardPiece):
            return freeBoardPiece
        return None