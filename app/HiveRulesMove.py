from typing import List, Tuple, Optional
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Directions import Direction
from app.Coordinate import Coordinate

class HiveRulesMove:

  def __init__(self, board: HiveBoard) -> None:
    self.board = board

  def addMovementMoves(self, moves: List[BoardPiece], playerOneTurn: bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return moves
    
    if(playerOneTurn):
        queenP1 = self.board.findPiece(self.board.pieces.QueenBeeP1)
        if queenP1 is not None:
          moves.append(queenP1.pieceToMove(Direction.UP_LEFT))

    if(not playerOneTurn):
        queenP2 = self.board.findPiece(self.board.pieces.QueenBeeP2)
        if queenP2 is not None:
          moves.append(queenP2.pieceToMove(Direction.UP_LEFT))

    return moves

  def moveablePieces(self, playerOneTurn:bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return []

    moveablePieces: List[BoardPiece] = []
    playerBoardPieces = self.board.getPlayerBoardPieces(playerOneTurn)
    for playerBoardPiece in playerBoardPieces:
      bridgingPieces = self.getBridgingPieces(playerBoardPiece)
      if bridgingPieces is None or not self.isConnectionBetweenPieces(bridgingPieces):
        moveablePieces.append(playerBoardPiece)

    return moveablePieces
  
  def isConnectionBetweenPieces(self, boardPieces: Tuple[BoardPiece, BoardPiece]) -> bool:
    connectionCoordinate: List[Coordinate] = []
    connectionCount = self.getCoonectionCount(boardPieces[0], connectionCoordinate)

    return boardPieces[1].coordinate in connectionCount

  def getCoonectionCount(self, boarPiece: BoardPiece, connectionCoordinate: List[Coordinate]) -> List[Coordinate]:
    if boarPiece.coordinate in connectionCoordinate:
      return connectionCoordinate
      
    connectionCoordinate.append(boarPiece.coordinate)

    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.LEFT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.UP_LEFT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.UP_RIGHT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.RIGHT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.DOWN_RIGHT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.DOWN_LEFT, boarPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getCoonectionCount(neighboardPiece, connectionCoordinate)

    return connectionCoordinate

  def getBridgingPieces(self, boardPiece: BoardPiece) -> Optional[Tuple[BoardPiece, BoardPiece]]:

    navigationCircle = [
      Direction.LEFT,
      Direction.UP_LEFT,
      Direction.UP_RIGHT,
      Direction.RIGHT,
      Direction.DOWN_RIGHT,
      Direction.DOWN_LEFT
    ]
    pieceCoordinate = boardPiece.coordinate
    gapCount = 0
    findGap = self.board.getBoardPiece(self.board.navigate(navigationCircle[5], pieceCoordinate)) != None

    connectionPieces: List[BoardPiece] = []
    for direction in navigationCircle:
      neighbourPiece: Optional[BoardPiece] = self.board.getBoardPiece(self.board.navigate(direction, pieceCoordinate))
      if neighbourPiece is not None and not findGap:
        connectionPieces.append(boardPiece)
        findGap = True

      elif neighbourPiece is None and findGap:
        findGap = False
        gapCount += 1

    if gapCount == 2:
      return (connectionPieces[0], connectionPieces[1])
      
    return None
