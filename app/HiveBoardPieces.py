from __future__ import annotations

from typing import List, Optional, TYPE_CHECKING
from app.PieceBuilder import PieceBuilder

if TYPE_CHECKING:
  from app.Piece import Piece

class HiveBoardPieces:

  def __init__(self) -> None:
    self._freePiecesP1: List[Piece] = [
      PieceBuilder().QueenBee_P1().Build(),
      PieceBuilder().Grasshopper_0_P1().Build(),
      PieceBuilder().Grasshopper_1_P1().Build(),
      PieceBuilder().Grasshopper_2_P1().Build(),
      PieceBuilder().Spider_0_P1().Build(),
      PieceBuilder().Spider_1_P1().Build(),
      PieceBuilder().Ant_0_P1().Build(),
      PieceBuilder().Ant_1_P1().Build(),
      PieceBuilder().Ant_2_P1().Build(),
      PieceBuilder().Beetle_0_P1().Build(),
      PieceBuilder().Beetle_1_P1().Build()
    ]

    self._freePiecesP2: List[Piece] = [
      PieceBuilder().QueenBee_P2().Build(),
      PieceBuilder().Grasshopper_0_P2().Build(),
      PieceBuilder().Grasshopper_1_P2().Build(),
      PieceBuilder().Grasshopper_2_P2().Build(),
      PieceBuilder().Spider_0_P2().Build(),
      PieceBuilder().Spider_1_P2().Build(),
      PieceBuilder().Ant_0_P2().Build(),
      PieceBuilder().Ant_1_P2().Build(),
      PieceBuilder().Ant_2_P2().Build(),
      PieceBuilder().Beetle_0_P2().Build(),
      PieceBuilder().Beetle_0_P2().Build()
    ]

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

  def removeFromFreePieces(self, piece: Piece) -> None:
      freeBoardPiece = self.findFreePiece(piece)
      if freeBoardPiece is not None:
        if(freeBoardPiece.firstPlayer):
          self._freePiecesP1.remove(freeBoardPiece)
        else:
          self._freePiecesP2.remove(freeBoardPiece)

  def findFreePiece(self, piece: Piece) -> Optional[Piece]:
      if(piece.firstPlayer):
        for freeBoardPiece in self._freePiecesP1:
          if(piece == freeBoardPiece):
            return freeBoardPiece
        return None
      else:
        for freeBoardPiece in self._freePiecesP2:
          if(piece == freeBoardPiece):
            return freeBoardPiece
        return None