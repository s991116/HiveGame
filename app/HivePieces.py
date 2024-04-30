from typing import List
from app.Piece import Piece
from app.Creatures import Creatures
class HivePieces:
  def __init__(self) -> None:
    self.QueenBeeP1       = Piece(True, Creatures.QueenBee, 0)
    self.Grasshopper_0_P1 = Piece(True, Creatures.Grasshopper, 0)
    self.Grasshopper_1_P1 = Piece(True, Creatures.Grasshopper, 1)
    self.Grasshopper_2_P1 = Piece(True, Creatures.Grasshopper, 2)
    self.Spider_0_P1      = Piece(True, Creatures.Spider, 0)
    self.Spider_1_P1      = Piece(True, Creatures.Spider, 1)
    self.Ant_0_P1         = Piece(True, Creatures.SoldierAnt, 0)
    self.Ant_1_P1         = Piece(True, Creatures.SoldierAnt, 1)
    self.Ant_2_P1         = Piece(True, Creatures.SoldierAnt, 2)
    self.Beetle_0_P1      = Piece(True, Creatures.Beetle, 0)
    self.Beetle_1_P1      = Piece(True, Creatures.Beetle, 1)    

    self.QueenBeeP2       = Piece(False, Creatures.QueenBee, 0)
    self.Grasshopper_0_P2 = Piece(False, Creatures.Grasshopper, 0)
    self.Grasshopper_1_P2 = Piece(False, Creatures.Grasshopper, 1)
    self.Grasshopper_2_P2 = Piece(False, Creatures.Grasshopper, 2)
    self.Spider_0_P2      = Piece(False, Creatures.Spider, 0)
    self.Spider_1_P2      = Piece(False, Creatures.Spider, 1)
    self.Ant_0_P2         = Piece(False, Creatures.SoldierAnt, 0)
    self.Ant_1_P2         = Piece(False, Creatures.SoldierAnt, 1)
    self.Ant_2_P2         = Piece(False, Creatures.SoldierAnt, 2)
    self.Beetle_0_P2      = Piece(False, Creatures.Beetle, 0)
    self.Beetle_1_P2      = Piece(False, Creatures.Beetle, 1)

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

    if playerOne:
      freePieces = self._freePiecesP1
    else:
      freePieces = self._freePiecesP2
    
    for freePiece in freePieces:
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