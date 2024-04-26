from typing import Tuple, Dict, List
from Directions import Direction
from Piece import Piece
from Creatues import Creatues
from Position import Position
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
      self._board: list[Tuple[Piece, Position]] = []
      self._centerCoordinate: Coordinate = Coordinate(0,0)

    def getBoard(self) -> List[Tuple[Piece, Position]]:    
      return self._board
  
    def isEmpty(self) -> bool:
      return len(self._board) == 0

    def setPiece(self, move: Tuple[Piece, Position]) -> None:
      self._board.append(move)
      self._normalizePosition()

    def _normalizePosition(self) -> None:
      queenBeeP1 = Piece(True, Creatues.QueenBee, 0)
      positions = self._getPositionForPiece(queenBeeP1)
      if(len(positions) > 0):
        self._calibratePosition(positions[0])
      pass

    def _getPositionForPiece(self, piece: Piece) -> List[Position]:
      for (boardPiece, boardPosition) in self._board:
        if(piece == boardPiece):
          return [boardPosition]     
      return []
      
    def _calibratePosition(self, Position: Position) -> None:
      for (_, boardPosition) in self._board:
        boardPosition.offset(Position.coordinate)


    def getCenterCoordinate(self) -> Coordinate:
      return self._centerCoordinate

    _shortPrint: Dict[Creatues, str] = {
        Creatues.Beetle: "B",
        Creatues.Grasshopper: "G",
        Creatues.QueenBee: "Q",
        Creatues.SoldierAnt: "A",
        Creatues.Spider: "S",
        Creatues.Mosquity: "M",
        Creatues.Ladybug: "L",        
    }

    def setPosition(self, boardPrint: str):
      boardPrintLines = boardPrint.splitlines()
      self._board = []
      position = Position(Coordinate(0,0))
      for boardPrintLine in boardPrintLines:
        boardPrintLineReversed = boardPrintLine[::-1]
        for pieaceLetter in boardPrintLineReversed:
          if pieaceLetter.isalpha():
            creature = next(key for key, value in self._shortPrint.items() if value == pieaceLetter.upper())
            firstPlayer = pieaceLetter.isupper()
            piece = Piece(firstPlayer, creature, 0)
            piecePosition: tuple[Piece, Position] = (piece, position)
            position = self.navigate(Direction.LEFT, position)
            self.setPiece(piecePosition)
    
    def navigate(self, direction: Direction, position: Position) -> Position:
      (xstep, ystep) = self._directionVector[direction]
      return Position(Coordinate(position.coordinate.x+xstep, position.coordinate.y+ystep))

    def printBoard(self) -> str:
      boardPrint: str = ""
      self._board.sort(key=self._boardPositionSorting)
      firstPieceInLine = True
      for (piece, _) in self._board:
        if piece.firstPlayer:
          piecePrint = self._shortPrint[piece.type].upper()
        else:
          piecePrint = self._shortPrint[piece.type].lower()

        if firstPieceInLine:
          boardPrint = boardPrint + piecePrint
          firstPieceInLine = False
        else:
          boardPrint = boardPrint + "|" + piecePrint
      return boardPrint
  
    def _boardPositionSorting(self, pieces: Tuple[Piece, Position]) -> int:
      _, position = pieces
      return position.coordinate.y*100+position.coordinate.x


