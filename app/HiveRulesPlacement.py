from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Coordinate import Coordinate

class HiveRulesPlacement:

  def __init__(self, board: HiveBoard) -> None:
    self.board =  board
    
  def addPlacementMoves(self, moves: List[BoardPiece], playerOneTurn: bool) -> List[BoardPiece]:
    freePlacements = self.getLegalPlacement(playerOneTurn)
      
    for freePlacement in freePlacements:
      if(not (self.straightLine() and not self.downCoordinate(freePlacement))):      
        playablePieces = self.board.playableFreePieces(playerOneTurn)
        for playablePiece in playablePieces:
          moves.append(BoardPiece(playablePiece, freePlacement))
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