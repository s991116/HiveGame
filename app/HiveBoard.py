from typing import Dict, List, Tuple, Optional
from app.Directions import Direction
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatures import Creatures
from app.Coordinate import Coordinate
from app.HivePieces import HivePieces
from itertools import groupby

class HiveBoard:
    
    def __init__(self) -> None:
      self._board: list[BoardPiece] = []
      self.pieces = HivePieces()
      self.centerCoordinate: Coordinate = Coordinate(0,0)
  
    def getBoard(self) -> List[BoardPiece]:    
      return self._board

    def isEmpty(self) -> bool:
      return len(self._board) == 0

    def movePiece(self, move: BoardPiece) -> None:
      self._setPiece(move)
      self._normalizePosition()

    def _setPiece(self, move: BoardPiece) -> None:
      self.pieces.removeFromFreePieces(move.piece)
      self._board.append(move)

    def findPiece(self, piece: Piece) -> Optional[BoardPiece]:
      for boardPiece in self._board:
        if(boardPiece.samePiece(piece)):
          return boardPiece
      return None

    def getPlayerBoardPieces(self, firstPlayer: bool) -> List[BoardPiece]:
      playerBoardPieces: List[BoardPiece] = []
      for boardPiece in self._board:
        if boardPiece.piece.firstPlayer == firstPlayer:
          playerBoardPieces.append(boardPiece)

      return playerBoardPieces

    def isPlaceFree(self, coordinate: Coordinate) -> bool:
      for boardPiece in self._board:
        if boardPiece.coordinate == coordinate:
          return False
      return True

    def getBoardPiece(self, coordinate:Coordinate) -> Optional[BoardPiece]:
      for boardPiece in self._board:
        if boardPiece.coordinate == coordinate:
          return boardPiece
      return None

    def isPlacePlayerPiece(self, coordinate: Coordinate, player: bool) -> bool:
      for boardPiece in self._board:
        if boardPiece.coordinate == coordinate and boardPiece.piece.firstPlayer == player:
          return True
      return False

    def playableFreePieces(self, firstPlayer:bool) -> List[Piece]:
      return self.pieces.playableFreePieces(firstPlayer)

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
      findGap = self.getBoardPiece(self.navigate(navigationCircle[5], pieceCoordinate)) != None

      connectionPieces: List[BoardPiece] = []
      for direction in navigationCircle:
        neighbourPiece: Optional[BoardPiece] = self.getBoardPiece(self.navigate(direction, pieceCoordinate))
        if neighbourPiece is not None and not findGap:
          connectionPieces.append(boardPiece)
          findGap = True

        elif neighbourPiece is None and findGap:
          findGap = False
          gapCount += 1

      if gapCount == 2:
        return (connectionPieces[0], connectionPieces[1])
      
      return None

    def isConnectionBetweenPieces(self, boardPieces: Tuple[BoardPiece, BoardPiece]) -> bool:
      connectionCoordinate: List[Coordinate] = []
      connectionCount = self.getCoonectionCount(boardPieces[0], connectionCoordinate)

      return boardPieces[1].coordinate in connectionCount

    def getCoonectionCount(self, boarPiece: BoardPiece, connectionCoordinate: List[Coordinate]) -> List[Coordinate]:
      if boarPiece.coordinate in connectionCoordinate:
        return connectionCoordinate
      
      connectionCoordinate.append(boarPiece.coordinate)

      neighboardPiece = self.getBoardPiece(self.navigate(Direction.LEFT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
      neighboardPiece = self.getBoardPiece(self.navigate(Direction.UP_LEFT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
      neighboardPiece = self.getBoardPiece(self.navigate(Direction.UP_RIGHT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
      neighboardPiece = self.getBoardPiece(self.navigate(Direction.RIGHT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
      neighboardPiece = self.getBoardPiece(self.navigate(Direction.DOWN_RIGHT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)
      neighboardPiece = self.getBoardPiece(self.navigate(Direction.DOWN_LEFT, boarPiece.coordinate))
      if(neighboardPiece is not None):
        return self.getCoonectionCount(neighboardPiece, connectionCoordinate)

      return connectionCoordinate

    def _normalizePosition(self) -> None:
      piece = self.findPiece(self.pieces.QueenBeeP1)
      if(piece is not None):
        self._calibratePositions(piece.coordinate)
      pass
      
    def _calibratePositions(self, offset: Coordinate) -> None:
      for piece in self._board:
          piece.coordinate = self._offsetCoordinate(offset, piece.coordinate)

    def _offsetCoordinate(self, offset: Coordinate, coordinate: Coordinate):
      x = coordinate.x - offset.x
      y = coordinate.y - offset.y
      return Coordinate(x,y)

    _shortPrint: Dict[Creatures, str] = {
        Creatures.Beetle: "B",
        Creatures.Grasshopper: "G",
        Creatures.QueenBee: "Q",
        Creatures.SoldierAnt: "A",
        Creatures.Spider: "S",
        Creatures.Mosquity: "M",
        Creatures.Ladybug: "L",        
    }

    def setupPosition(self, boardPrintLines: List[str]):
      self._board = []
      lineNr = 0
      for boardPrintLine in boardPrintLines:
        boardPrintLineReversed = boardPrintLine[::-1]
        pieceCoordinate = Coordinate(0,lineNr)
        for stringIndex in range(len(boardPrintLineReversed)):
          indexString = boardPrintLineReversed[stringIndex]
          if indexString.isdigit():
            index = int(indexString)
            pieaceLetter = boardPrintLineReversed[stringIndex+1]
            creature = next(key for key, value in self._shortPrint.items() if value == pieaceLetter.upper())
            firstPlayer = pieaceLetter.isupper()
            piece = BoardPiece(Piece(firstPlayer, creature, index), pieceCoordinate)
            self._setPiece(piece)
            pieceCoordinate = self._offsetCoordinate(Coordinate(1,0), pieceCoordinate)
        lineNr += 1
      self._normalizePosition()
    
    def navigate(self, direction: Direction, coordinate: Coordinate) -> Coordinate:
      if direction == Direction.LEFT:
        return Coordinate(coordinate.x-1, coordinate.y)
      elif direction == Direction.RIGHT:
        return Coordinate(coordinate.x+1, coordinate.y)
      
      if(coordinate.y % 2 == 0):
        xOffset = -1
      else:
        xOffset = 0

      if direction == Direction.DOWN_LEFT:
        return Coordinate(coordinate.x   + xOffset, coordinate.y-1)
      elif direction == Direction.DOWN_RIGHT:
        return Coordinate(coordinate.x+1 + xOffset, coordinate.y-1)
      if direction == Direction.UP_LEFT:
        return Coordinate(coordinate.x   + xOffset, coordinate.y+1)
      elif direction == Direction.UP_RIGHT:
        return Coordinate(coordinate.x+1 + xOffset, coordinate.y+1)

    def getNeighbourCoordinates(self, centerCoordinate: Coordinate) -> List[Coordinate]:
      neighbourCoordinates =  [
              self.navigate(Direction.DOWN_LEFT, centerCoordinate),
              self.navigate(Direction.DOWN_RIGHT,centerCoordinate),
              self.navigate(Direction.UP_LEFT,   centerCoordinate),
              self.navigate(Direction.UP_RIGHT,  centerCoordinate),
              self.navigate(Direction.LEFT,      centerCoordinate),
              self.navigate(Direction.RIGHT,     centerCoordinate),
              ]
      return neighbourCoordinates

    def printBoard(self) -> str:
      self._board.sort(key=self._boardPositionSorting)
      boardPrint = "\n"
      for y_position, boardPiecesLines in groupby(self._board, lambda x: x.coordinate.y):
        boardPrintLine1: str = ""
        boardPrintLine2: str = ""
        boardPrintLine3: str = ""
        if(y_position % 2 == 1):
          boardPrintLine1: str = "  "
          boardPrintLine2: str = "  "
          boardPrintLine3: str = "  "

        boardPiecesLines = sorted(boardPiecesLines, key=lambda x: x.coordinate.x)
        min_x_position = -10
        for boardPiece in boardPiecesLines:
          for _ in range(1, boardPiece.coordinate.x - min_x_position):
            boardPrintLine1 += "    "
            boardPrintLine2 += "    "
            boardPrintLine3 += "    "
          min_x_position = boardPiece.coordinate.x+1
          piece = boardPiece.piece
           
          if piece.firstPlayer:
            piecePrint = self._shortPrint[piece.creature].upper()
          else:
            piecePrint = self._shortPrint[piece.creature].lower()

          boardPrintLine1 += "/--\\"
          boardPrintLine2 += "|" + piecePrint + str(piece.index) + "|"
          boardPrintLine3 += "\\--/"
      
        boardPrint += boardPrintLine1 + "\n" + boardPrintLine2 + "\n" + boardPrintLine3 + "\n"
      
      return boardPrint
  
    def _boardPositionSorting(self, piece: BoardPiece) -> int:
      return piece.coordinate.y*100+piece.coordinate.x



#   /--\/--\/--\/--\
#   |B1||g1||B1||g1|
#   \--/\--/\--/\--/
#     /--\/--\/--\/--\
#     |B1||g1||B1||g1|
#     \--/\--/\--/\--/
#   /--\/--\/--\/--\
#   |B1||g1||B1||g1|
#   \--/\--/\--/\--/

#       /----\/----\/----\/----\/----\/----\
#+1     |-4 1||-3 1||-2 1||-1 1|| 0 1|| 1 1|
#       \----/\----/\----/\----/\----/\----/
#    /----\/----\/----\/----\/----\/----\
#0   |-4 0||-3 0||-2 0||-1 0|| 0 0|| 1 0|
#    \----/\----/\----/\----/\----/\----/
#        /----\/----\/----\/----\/----\/----\
#-1     |-4-1||-3-1||-2-1||-1-1|| 0-1|| 1-1|
#0      \----/\----/\----/\----/\----/\----/

# Left       = -1, 0  | -1, 0
# right      = +1, 0  | +1, 0
# Up_Left    =  0,+1  | -1,+1 | -1
# Up_Right   = +1,+1  |  0,+1 | -1
# Down_Left  =  0,-1  | -1,-1 | -1
# Down_Right = +1,-1  |  0,-1 | -1

#(-1,0)-(0,0)-(0,1)?

#Placement Coor (-1,0)
#-2 -1
#-1 -1
#-2  1
#-1  1
#-2  0
# 0  0

#-2 -1
#-2  0
#-2  1
#-1 -1?

#Neighbour coor (-1,-1)
#-1  0 X
# 0  0 X
#-2 -1 X
# 0 -1 X
#-1 -2 X
# 0 -2 X