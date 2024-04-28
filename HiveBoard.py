from typing import Tuple, Dict, List
from Directions import Direction
from Piece import Piece
from Creatues import Creatues
from Coordinate import Coordinate
from HivePieces import HivePieces

class HiveBoard:

    _directionVector: Dict[Direction, Tuple[int,int]] = {
     Direction.LEFT:       (-1, 0),
     Direction.RIGHT:      ( 1, 0),
     Direction.UP_LEFT:    ( 1, 1),
     Direction.UP_RIGHT:   ( 0, 1),
     Direction.DOWN_LEFT:  (-1,-1),
     Direction.DOWN_RIGHT: ( 0,-1)}
    
    def __init__(self) -> None:
      self._board: list[Piece] = []
      self._pieces = HivePieces()
      self.centerCoordinate: Coordinate = Coordinate(0,0)
  
    def getBoard(self) -> List[Piece]:    
      return self._board

    def isEmpty(self) -> bool:
      return len(self._board) == 0

    def setPiece(self, move: Piece) -> None:
      self._setPiece(move)
      self._normalizePosition()

    def _setPiece(self, move: Piece) -> None:
      self._pieces.removeFromFreePieces(move)
      self._board.append(move)

    def findPiece(self, piece: Piece) -> List[Piece]:
      for boardPiece in self._board:
        if(boardPiece.sameKind(piece)):
          return[boardPiece]
      return []

    def freePieces(self, firstPlayer: bool) -> List[Piece]:
      return self._pieces.freePieces(firstPlayer)

    def PlayablePieces(self, firstPlayer:bool) -> List[Piece]:
      return self._pieces.PlayablePieces(firstPlayer)

    def _normalizePosition(self) -> None:
      queenBeeP1 = Piece(True, Creatues.QueenBee, 0, Coordinate(0,0))
      piece = self.findPiece(queenBeeP1)
      if(len(piece) > 0):
        self._calibratePositions(piece[0].coordinate)
      pass
      
    def _calibratePositions(self, offset: Coordinate) -> None:
      for piece in self._board:
          piece.coordinate = self._offsetCoordinate(offset, piece.coordinate)

    def _offsetCoordinate(self, offset: Coordinate, coordinate: Coordinate):
      x = coordinate.x - offset.x
      y = coordinate.y - offset.y
      return Coordinate(x,y)

    _shortPrint: Dict[Creatues, str] = {
        Creatues.Beetle: "B",
        Creatues.Grasshopper: "G",
        Creatues.QueenBee: "Q",
        Creatues.SoldierAnt: "A",
        Creatues.Spider: "S",
        Creatues.Mosquity: "M",
        Creatues.Ladybug: "L",        
    }

    def setupPosition(self, boardPrint: str):
      boardPrintLines = boardPrint.splitlines()
      self._board = []
      pieceCoordinate = Coordinate(0,0)
      for boardPrintLine in boardPrintLines:
        boardPrintLineReversed = boardPrintLine[::-1]
        for stringIndex in range(len(boardPrintLineReversed)):
          indexString = boardPrintLineReversed[stringIndex]
          if indexString.isdigit():
            index = int(indexString)
            pieaceLetter = boardPrintLineReversed[stringIndex+1]
            creature = next(key for key, value in self._shortPrint.items() if value == pieaceLetter.upper())
            firstPlayer = pieaceLetter.isupper()
            piece = Piece(firstPlayer, creature, index, pieceCoordinate)
            self._setPiece(piece)
            pieceCoordinate = self._offsetCoordinate(Coordinate(1,0), pieceCoordinate)
      self._normalizePosition()
    
    def navigate(self, direction: Direction, coordinate: Coordinate) -> Coordinate:
      (xstep, ystep) = self._directionVector[direction]
      return Coordinate(coordinate.x+xstep, coordinate.y+ystep)

    def printBoard(self) -> str:
      self._board.sort(key=self._boardPositionSorting)
      boardPrintLine1: str = ""
      boardPrintLine2: str = ""
      boardPrintLine3: str = ""

      for piece in self._board:
        if piece.firstPlayer:
          piecePrint = self._shortPrint[piece.creature].upper()
        else:
          piecePrint = self._shortPrint[piece.creature].lower()

        boardPrintLine1 += "/--\\"
        boardPrintLine2 += "|" + piecePrint + str(piece.index) + "|"
        boardPrintLine3 += "\\--/"
      return boardPrintLine1 + "\n" + boardPrintLine2 + "\n" + boardPrintLine3 + "\n"
  
    def _boardPositionSorting(self, piece: Piece) -> int:
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
