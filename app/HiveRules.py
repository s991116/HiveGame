from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Creatures import Creatures
from app.Directions import Direction
from app.Coordinate import Coordinate

class HiveRules:

  def __init__(self, board: HiveBoard) -> None:
    self.playerOneTurn = True
    self.board = board
    self.QueenP1Placed = False
    self.QueenP2Placed = False

  def playMove(self, move: BoardPiece):  
    
    if(move.piece.creature == Creatures.QueenBee):
      if(self.playerOneTurn):
        self.QueenP1Placed = True
      else:
        self.QueenP2Placed = True

    self.board.movePiece(move)
    self.playerOneTurn = not self.playerOneTurn

  def getValidMoves(self) -> List[BoardPiece]:

    moves:list[BoardPiece] = []

    if(len(self.board.getBoard())<=1):
      if(self.playerOneTurn):
        startPosition = self.board.centerCoordinate
      else:
        startPosition = self.board.navigate(Direction.LEFT, self.board.centerCoordinate)
        
      for playablePiece in self.board.playableFreePieces(self.playerOneTurn):
        moves.append(BoardPiece(playablePiece, startPosition))
      return moves

    moves = self.addPlacementMoves(moves)
    moves = self.addMovementMoves(moves)

    return moves

  def addMovementMoves(self, moves: List[BoardPiece]) -> List[BoardPiece]:
    if(self.playerOneTurn and self.QueenP1Placed):
        QueenP1 = self.board.pieces.QueenBeeP1
        moves.append(self.board.findPiece(QueenP1)[0].pieceToMove(Direction.UP_LEFT))

    if(not self.playerOneTurn and self.QueenP2Placed):
        QueenP2 = self.board.pieces.QueenBeeP1
        moves.append(self.board.findPiece(QueenP2)[0].pieceToMove(Direction.UP_LEFT))

    return moves

  def addPlacementMoves(self, moves: List[BoardPiece]) -> List[BoardPiece]:
    freePlacements = self.getLegalPlacement(self.playerOneTurn)
      
    for freePlacement in freePlacements:
      if(not (self.straightLine() and not self.downCoordinate(freePlacement))):      
        playablePieces = self.board.playableFreePieces(self.playerOneTurn)
        for playablePiece in playablePieces:
          moves.append(BoardPiece(playablePiece, freePlacement))
    return moves

  def getLegalPlacement(self, firstPlayer:bool) -> List[Coordinate]:
    legalPlacement: List[Coordinate] = []
    playerBoardPieces = self.board.getPlayerBoardPieces(firstPlayer)
    for playerBoardPiece in playerBoardPieces:
      placementCoordinates = self.board.getNeighbourCoordinates(playerBoardPiece.coordinate)
      for placementCoordinate in placementCoordinates:
        if self.board.isPlaceFree(placementCoordinate) and self.noNeighbourOppositePlayerPiece(placementCoordinate, not firstPlayer):
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

  def updatePosition(self):
    Q1P1 = self.board.pieces.QueenBeeP1
    Q1P2 = self.board.pieces.QueenBeeP2

    if(len(self.board.findPiece(Q1P1)) > 0):
      self.QueenP1Placed = True

    if(len(self.board.findPiece(Q1P2)) > 0):
      self.QueenP2Placed = True      