from typing import List
from app.Piece import Piece
from app.Creatues import Creatues

class HivePieces:
  def __init__(self) -> None:
    self._freePiecesP1 = self.startingPieces(True)
    self._freePiecesP2 = self.startingPieces(False)

  def startingPieces(self, firstPlayer:bool):
    startingPieces = [
      Piece(firstPlayer, Creatues.QueenBee,     0),
      Piece(firstPlayer, Creatues.Grasshopper,  0),
      Piece(firstPlayer, Creatues.Grasshopper,  1),
      Piece(firstPlayer, Creatues.Grasshopper,  2),
      Piece(firstPlayer, Creatues.Spider,       0),
      Piece(firstPlayer, Creatues.Spider,       1),
      Piece(firstPlayer, Creatues.SoldierAnt,   0),
      Piece(firstPlayer, Creatues.SoldierAnt,   1),
      Piece(firstPlayer, Creatues.SoldierAnt,   2),
      Piece(firstPlayer, Creatues.Beetle,       0),
      Piece(firstPlayer, Creatues.Beetle,       1),
    ]
    return startingPieces

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