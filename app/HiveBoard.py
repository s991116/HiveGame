from typing import Tuple, Dict, List
from app.Directions import Direction
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatues import Creatues
from app.Coordinate import Coordinate
from app.HivePieces import HivePieces
from itertools import groupby

class HiveBoard:

    _directionVector: Dict[Direction, Tuple[int,int]] = {
     Direction.LEFT:       (-1, 0),
     Direction.RIGHT:      ( 1, 0),
     Direction.UP_LEFT:    ( 1, 1),
     Direction.UP_RIGHT:   ( 0, 1),
     Direction.DOWN_LEFT:  (-1,-1),
     Direction.DOWN_RIGHT: ( 0,-1)}
    
    def __init__(self) -> None:
      self._board: list[BoardPiece] = []
      self.pieces = HivePieces()
      self.centerCoordinate: Coordinate = Coordinate(0,0)
  
    def getBoard(self) -> List[BoardPiece]:    
      return self._board

    def isEmpty(self) -> bool:
      return len(self._board) == 0

    def setPiece(self, move: BoardPiece) -> None:
      self._setPiece(move)
      self._normalizePosition()

    def _setPiece(self, move: BoardPiece) -> None:
      self.pieces.removeFromFreePieces(move.piece)
      self._board.append(move)

    def findPiece(self, piece: Piece) -> List[BoardPiece]:
      for boardPiece in self._board:
        if(boardPiece.samePiece(piece)):
          return[boardPiece]
      return []

    def playableFreePieces(self, firstPlayer:bool) -> List[Piece]:
      return self.pieces.playableFreePieces(firstPlayer)

    def _normalizePosition(self) -> None:
      piece = self.findPiece(self.pieces.QueenBeeP1)
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
      (xstep, ystep) = self._directionVector[direction]
      return Coordinate(coordinate.x+xstep, coordinate.y+ystep)

    def printBoard(self) -> str:
      self._board.sort(key=self._boardPositionSorting)
      boardPrint = ""
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