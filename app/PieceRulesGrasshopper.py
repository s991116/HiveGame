from __future__ import annotations
from typing import List
from app.PieceRules import PieceRules
from app.Coordinate import Coordinate
import app.BoardPiece as BP
import app.HiveBoard as HB
import app.HivePieces as HP

class PieceRulesGrasshopper(PieceRules):

  def getMoves(self, boardPiece: BP.BoardPiece, board: HB.HiveBoard) -> List[BP.BoardPiece]:
    return [HP.HivePieces.CreateCloneWithCoordinate(boardPiece, Coordinate(0,0))]
