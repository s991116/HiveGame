from __future__ import annotations

from typing import List
from app.HiveBoard import HiveBoard
from app.HivePieces import HivePieces
from app.BoardPiece import BoardPiece
from app.Coordinate import Coordinate

class HiveRulesPlacement:

  def __init__(self, board: HiveBoard) -> None:
    self.board =  board
    
  def getPlacementMoves(self, playerOneTurn: bool) -> List[BoardPiece]:
    freePlacements = self.getLegalPlacement(playerOneTurn)

    moves: List[BoardPiece] = []  
    for freePlacement in freePlacements:
      if(not (self.straightLine() and not self.downCoordinate(freePlacement))):      
        playablePieces = self.board.playableFreePieces(playerOneTurn)
        for playablePiece in playablePieces:
          moves.append(HivePieces.CreateCloneWithCoordinate(playablePiece, freePlacement))
    return moves

  def getLegalPlacement(self, playerOneTurn: bool) -> List[Coordinate]:
    legalPlacement: List[Coordinate] = []
    playerBoardPieces = self.board.getPlayerBoardPieces(playerOneTurn)
    for playerBoardPiece in playerBoardPieces:
      placementCoordinates = self.board.getNeighbourCoordinates(playerBoardPiece.coordinate)
      for placementCoordinate in placementCoordinates:
        if self.board.isPlaceFree(placementCoordinate) and self.noNeighbourOppositePlayerPiece(placementCoordinate, not playerOneTurn):
          legalPlacement.append(placementCoordinate)
      
    legalPlacement = self.removeDubpliceCoordinate(legalPlacement)
    return legalPlacement

  def noNeighbourOppositePlayerPiece(self, centerCoordinate: Coordinate, oppositPlayer: bool) -> bool:
    neighbourCoordinates = self.board.getNeighbourCoordinates(centerCoordinate)
    for neighbourCoordinate in neighbourCoordinates:
      if(self.board.isPlacePlayerPiece(neighbourCoordinate, oppositPlayer)):
        return False
    return True

  def straightLine(self) -> bool:
    for boardPiece in self.board.getBoard():
      if boardPiece.coordinate.y != 0:
        return False
    return True

  def removeDubpliceCoordinate(self, legalPlacement: List[Coordinate]):
    withoutDublicate = list(set(legalPlacement))
    return withoutDublicate
  
  def downCoordinate(self, coordinate: Coordinate) -> bool:
    return coordinate.y != -1