from typing import List, Optional
from app.PieceGrasshopper import PieceGrasshopper
from app.Piece import Piece
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

    self._freePiecesP1: List[Piece] = [
      self.QueenBee_P1.piece,
      self.Grasshopper_0_P1.piece,
      self.Grasshopper_1_P1.piece,
      self.Grasshopper_2_P1.piece,
      self.Spider_0_P1.piece,
      self.Spider_1_P1.piece,
      self.Ant_0_P1.piece,
      self.Ant_1_P1.piece,
      self.Ant_2_P1.piece,
      self.Beetle_0_P1.piece,
      self.Beetle_1_P1.piece,
    ]

    self._freePiecesP2: List[Piece] = [
      self.QueenBee_P2.piece,
      self.Grasshopper_0_P2.piece,
      self.Grasshopper_1_P2.piece,
      self.Grasshopper_2_P2.piece,
      self.Spider_0_P2.piece,
      self.Spider_1_P2.piece,
      self.Ant_0_P2.piece,
      self.Ant_1_P2.piece,
      self.Ant_2_P2.piece,
      self.Beetle_0_P2.piece,
      self.Beetle_1_P2.piece,
    ]

  @staticmethod
  def CreatePiece(firstPlayer: bool, creature: Creatures, index: int, coordinate: Coordinate) -> BoardPiece:
    
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
  def CreatePieceWithCoordinate(piece: Piece, coordinate: Coordinate) -> BoardPiece:
    return HivePieces.CreatePiece(piece.firstPlayer, piece.creature, piece.index, coordinate)

  def playableFreePieces(self, playerOne:bool):
    playableCreatures: List[Piece] = []

    if playerOne:
      freePieces = self._freePiecesP1
    else:
      freePieces = self._freePiecesP2
    
    for piece in freePieces:
      foundPiece = False
      for playableCreature in playableCreatures:
        if(playableCreature.creature == piece.creature):
          foundPiece = True
          break

      if(not foundPiece):
        playableCreatures.append(piece)

    return playableCreatures

  def removeFromFreePieces(self, move: Piece) -> None:
      piece = self.findFreePiece(move)
      if piece is not None:
        if(move.firstPlayer):
          self._freePiecesP1.remove(piece)
        else:
          self._freePiecesP2.remove(piece)

  def findFreePiece(self, piece: Piece) -> Optional[Piece]:
      if(piece.firstPlayer):
        for freePiece in self._freePiecesP1:
          if(piece == freePiece):
            return freePiece
        return None
      else:
        for freePiece in self._freePiecesP2:
          if(piece == freePiece):
            return freePiece
        return None