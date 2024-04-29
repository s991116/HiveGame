from typing import List
from app.Piece import Piece
from app.Creatues import Creatues

class HivePieces:
  def __init__(self) -> None:
    self.QueenBeeP1       = Piece(True, Creatues.QueenBee, 0)
    self.Grasshopper_0_P1 = Piece(True, Creatues.Grasshopper, 0)
    self.Grasshopper_1_P1 = Piece(True, Creatues.Grasshopper, 1)
    self.Grasshopper_2_P1 = Piece(True, Creatues.Grasshopper, 2)
    self.Spider_0_P1      = Piece(True, Creatues.Spider, 0)
    self.Spider_1_P1      = Piece(True, Creatues.Spider, 1)
    self.Ant_0_P1         = Piece(True, Creatues.SoldierAnt, 0)
    self.Ant_1_P1         = Piece(True, Creatues.SoldierAnt, 1)
    self.Ant_2_P1         = Piece(True, Creatues.SoldierAnt, 2)
    self.Beetle_0_P1      = Piece(True, Creatues.Beetle, 0)
    self.Beetle_1_P1      = Piece(True, Creatues.Beetle, 1)    

    self.QueenBeeP2       = Piece(False, Creatues.QueenBee, 0)
    self.Grasshopper_0_P2 = Piece(False, Creatues.Grasshopper, 0)
    self.Grasshopper_1_P2 = Piece(False, Creatues.Grasshopper, 1)
    self.Grasshopper_2_P2 = Piece(False, Creatues.Grasshopper, 2)
    self.Spider_0_P2      = Piece(False, Creatues.Spider, 0)
    self.Spider_1_P2      = Piece(False, Creatues.Spider, 1)
    self.Ant_0_P2         = Piece(False, Creatues.SoldierAnt, 0)
    self.Ant_1_P2         = Piece(False, Creatues.SoldierAnt, 1)
    self.Ant_2_P2         = Piece(False, Creatues.SoldierAnt, 2)
    self.Beetle_0_P2      = Piece(False, Creatues.Beetle, 0)
    self.Beetle_1_P2      = Piece(False, Creatues.Beetle, 1)

    self._freePiecesP1 = [
      self.QueenBeeP1,
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

    self._freePiecesP2 = [
      self.QueenBeeP2,
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

  def playableFreePieces(self, playerOne:bool):
    playableCreatures: List[Piece] = []
      
    for freePiece in self._freePiecesP1:
      foundPiece = False
      for playableCreature in playableCreatures:
        if(playableCreature.creature == freePiece.creature):
          foundPiece = True
          break

      if(not foundPiece):
        playableCreatures.append(freePiece)

    return playableCreatures

  def removeFromFreePieces(self, move: Piece) -> None:
      piece = self.findFreePiece(move)
      if(len(piece) > 0):
        if(move.firstPlayer):
          self._freePiecesP1.remove(piece[0])
        else:
          self._freePiecesP2.remove(piece[0])

  def findFreePiece(self, piece: Piece) -> List[Piece]:
      if(piece.firstPlayer):
        for freePiece in self._freePiecesP1:
          if(piece == freePiece):
            return[freePiece]
        return []
      else:
        for freePiece in self._freePiecesP2:
          if(piece == freePiece):
            return[freePiece]
        return []