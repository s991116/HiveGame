from typing import List
from Piece import Piece
from Creatues import Creatues
from Coordinate import Coordinate

class HivePieces:
  def __init__(self) -> None:
    self._freePiecesP1 = self.startingPieces(True)
    self._freePiecesP2 = self.startingPieces(False)

  def startingPieces(self, firstPlayer:bool):
    c = Coordinate(0,0)
    freePieces = [
      Piece(firstPlayer, Creatues.QueenBee,     0, c),
      Piece(firstPlayer, Creatues.Grasshopper,  0, c),
      Piece(firstPlayer, Creatues.Grasshopper,  1, c),
      Piece(firstPlayer, Creatues.Grasshopper,  2, c),
      Piece(firstPlayer, Creatues.Spider,       0, c),
      Piece(firstPlayer, Creatues.Spider,       1, c),
      Piece(firstPlayer, Creatues.SoldierAnt,   0, c),
      Piece(firstPlayer, Creatues.SoldierAnt,   1, c),
      Piece(firstPlayer, Creatues.SoldierAnt,   2, c),
      Piece(firstPlayer, Creatues.Beetle,       0, c),
      Piece(firstPlayer, Creatues.Beetle,       1, c),
    ]
    return freePieces

  def PlayablePieces(self, playerOne:bool):
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

  def freePieces(self, firstPlayer: bool) -> List[Piece]:
    if (firstPlayer):
      return self._freePiecesP1
    else:
      return self._freePiecesP2

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
          if(piece.sameKind(freePiece)):
            return[freePiece]
        return []
      else:
        for freePiece in self._freePiecesP2:
          if(piece.sameKind(freePiece)):
            return[freePiece]
        return []