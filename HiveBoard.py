from typing import Tuple, Dict, List
from Directions import Direction
from Piece import Piece
from Creatues import Creatues
from Coordinate import Coordinate

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
      self.centerCoordinate: Coordinate = Coordinate(0,0)

    def getBoard(self) -> List[Piece]:    
      return self._board
  
    def isEmpty(self) -> bool:
      return len(self._board) == 0

    def setPiece(self, move: Piece) -> None:
      self._board.append(move)
      self._normalizePosition()

    def _normalizePosition(self) -> None:
      queenBeeP1 = Piece(True, Creatues.QueenBee, 0, Coordinate(0,0))
      coordinates = self._getPositionForPiece(queenBeeP1)
      if(len(coordinates) > 0):
        self._calibratePositions(coordinates[0])
      pass

    def _getPositionForPiece(self, piece: Piece) -> List[Coordinate]:
      for boardPiece in self._board:
        if(piece.sameKind(boardPiece)):
          return [boardPiece.coordinate]
      return []
      
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
        for pieaceLetter in boardPrintLineReversed:
          if pieaceLetter.isalpha():
            creature = next(key for key, value in self._shortPrint.items() if value == pieaceLetter.upper())
            firstPlayer = pieaceLetter.isupper()
            piece = Piece(firstPlayer, creature, 0, pieceCoordinate)
            self.setPiece(piece)
            pieceCoordinate = self._offsetCoordinate(Coordinate(1,0), pieceCoordinate)
      self._normalizePosition()
    
    def navigate(self, direction: Direction, coordinate: Coordinate) -> Coordinate:
      (xstep, ystep) = self._directionVector[direction]
      return Coordinate(coordinate.x+xstep, coordinate.y+ystep)

    def printBoard(self) -> str:
      boardPrint: str = ""
      self._board.sort(key=self._boardPositionSorting)
      firstPieceInLine = True
      for piece in self._board:
        if piece.firstPlayer:
          piecePrint = self._shortPrint[piece.creature].upper()
        else:
          piecePrint = self._shortPrint[piece.creature].lower()

        if firstPieceInLine:
          boardPrint = boardPrint + piecePrint
          firstPieceInLine = False
        else:
          boardPrint = boardPrint + "|" + piecePrint
      return boardPrint
  
    def _boardPositionSorting(self, piece: Piece) -> int:
      return piece.coordinate.y*100+piece.coordinate.x


