from __future__ import annotations

from typing import List, Tuple, Optional
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Directions import Direction
from app.Coordinate import Coordinate

class HiveRulesMove:

  def __init__(self, board: HiveBoard) -> None:
    self.board = board

  def getMovementMoves(self, playerOneTurn: bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return []
    
    moves: List[BoardPiece] = []
    moveableBoardPieces = self.moveablePieces(playerOneTurn, queenPlaced)
    for moveableBoardPiece in moveableBoardPieces:
      
      moves += moveableBoardPiece.getMoves(self.board)

    return moves

  def moveablePieces(self, playerOneTurn:bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return []

    moveablePieces: List[BoardPiece] = []
    playerBoardPieces = self.board.getPlayerBoardPieces(playerOneTurn)
    for playerBoardPiece in playerBoardPieces:
      if self.isTopPiece(playerBoardPiece):
        bridgingPieces = self.getBridgingPieces(playerBoardPiece)
        if bridgingPieces is None or self.isConnectionBetween2Pieces(bridgingPieces[0].coordinate, bridgingPieces[1].coordinate, playerBoardPiece.coordinate, [bridgingPieces[0].coordinate]):
          moveablePieces.append(playerBoardPiece)

    return moveablePieces
  
  def isTopPiece(self, boardPiece: BoardPiece) -> bool:
    return self.board.getTopLayer(boardPiece.coordinate) == boardPiece.layer

  def isConnectionBetweenPieces(self, boardPieces: Tuple[BoardPiece, BoardPiece]) -> bool:
    connectionCoordinate: List[Coordinate] = []
    connectionCount = self.getConnectionCount(boardPieces[0], connectionCoordinate)

    return boardPieces[1].coordinate in connectionCount


  def isConnectionBetween2Pieces(self, coordinateA: Coordinate, coordinateB: Coordinate, removedCoordinate: Coordinate, searchedCoordinates: List[Coordinate]) -> bool:
    if(coordinateA == coordinateB):
      return True
    
    directions = [Direction.LEFT, Direction.UP_LEFT, Direction.UP_RIGHT, Direction.RIGHT, Direction.DOWN_RIGHT, Direction.DOWN_LEFT]

    for searchDirection in directions:
      searchCoordinate = self.board.navigate(searchDirection, coordinateA)
      if searchCoordinate !=removedCoordinate:
        isCoordinateEmpty = self.board.isPlaceFree(searchCoordinate)  
        if not isCoordinateEmpty and searchCoordinate not in searchedCoordinates:
          searchedCoordinates.append(searchCoordinate)
          if self.isConnectionBetween2Pieces(searchCoordinate, coordinateB, removedCoordinate, searchedCoordinates):
            return True

    return False

  def getConnectionCount(self, boardPiece: BoardPiece, connectionCoordinate: List[Coordinate]) -> List[Coordinate]:
    if boardPiece.coordinate in connectionCoordinate:
      return connectionCoordinate
      
    connectionCoordinate.append(boardPiece.coordinate)

    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.LEFT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.UP_LEFT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.UP_RIGHT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.RIGHT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.DOWN_RIGHT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)
    neighboardPiece = self.board.getBoardPiece(self.board.navigate(Direction.DOWN_LEFT, boardPiece.coordinate))
    if(neighboardPiece is not None):
      return self.getConnectionCount(neighboardPiece, connectionCoordinate)

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
    endCoordinate = self.board.navigate(navigationCircle[5], pieceCoordinate)
    findGap = not self.board.isPlaceFree(endCoordinate)

    connectionPieces: List[BoardPiece] = []
    for direction in navigationCircle:
      neighbourPiece: Optional[BoardPiece] = self.board.getBoardPiece(self.board.navigate(direction, pieceCoordinate))
      if neighbourPiece is not None and not findGap:
        connectionPieces.append(neighbourPiece)
        findGap = True

      elif neighbourPiece is None and findGap:
        findGap = False
        gapCount += 1

    if gapCount == 2:
      return (connectionPieces[0], connectionPieces[1])
      
    return None