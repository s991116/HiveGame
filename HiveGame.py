from typing import List, Tuple, Dict
from Piece import Piece
from Creatues import Creatues
from Position import Position
from Directions import Direction

class HiveGame:

  _directionVector: Dict[Direction, Tuple[int,int]] = {
     Direction.LEFT:       (-1, 0),
     Direction.RIGHT:      ( 1, 0),
     Direction.UP_LEFT:    ( 1, 1),
     Direction.UP_RIGHT:   ( 0, 1),
     Direction.DOWN_LEFT:  (-1,-1),
     Direction.DOWN_RIGHT: ( 0,-1)}

  def __init__(self) -> None:
    
    self.playerPieces: list[Piece] = []
    for playerOne in [True, False]:
      self.playerPieces.append(Piece(playerOne, Creatues.QueenBee, 0))
      for index in range(0,3):
        self.playerPieces.append(Piece(playerOne, Creatues.Grasshopper, index))
      for index in range(0,3):
        self.playerPieces.append(Piece(playerOne, Creatues.SoldierAnt, index))
      for index in range(0,2):
        self.playerPieces.append(Piece(playerOne, Creatues.Spider, index))
      for index in range(0,2):
        self.playerPieces.append(Piece(playerOne, Creatues.Beetle, index))

    self.centerPosition: Position = Position(0,0)
    self._board: list[Tuple[Piece, Position]] = []
    self._playerOneTurn = True

  def setPiece(self, move: Tuple[Piece, Position]):
    self._playerOneTurn = not self._playerOneTurn
    self._board.append(move)

  def getValidMoves(self) -> List[Tuple[Piece, Position]]:
    moves:list[Tuple[Piece, Position]] = []
    if(self._playerOneTurn):
      if(len(self._board) == 0):
        for piece in self.playerPieces:
          if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):
            moves.append((piece, self.centerPosition))
      else:
        positions = [self._navigate(Direction.UP_RIGHT, self.centerPosition), self._navigate(Direction.RIGHT, self.centerPosition)]
        for position in positions:
          for piece in self.playerPieces:
            if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):
              moves.append((piece, position))

    else:
      for piece in self.playerPieces:
        if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):        
          moves.append((piece, self._navigate(Direction.LEFT, self.centerPosition)))

    return moves
  
  def getPlayerPieces(self, playerOne:bool) -> List[Piece]:
    pieces: list[Piece] = []
    for piece in self.playerPieces:
      if(piece.firstPlayer == playerOne and piece.index == 0):
        pieces.append(piece)
    return pieces

  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self._board
  
  def moveLeft(self) -> None:
    self.x = self.x-1

  def _navigate(self, direction: Direction, position: Position) -> Position:
    (xstep, ystep) = self._directionVector[direction]
    return Position(position.x+xstep, position.y+ystep)

  def setPosition(self, boardPrint: str, playerOneTurn: bool):
    boardPrintLines = boardPrint.splitlines()
    self._board = []
    position = Position(0,0)
    for boardPrintLine in boardPrintLines:
      boardPrintLineReversed = boardPrintLine[::-1]
      for pieaceLetter in boardPrintLineReversed:
        if pieaceLetter.isalpha():
          creature = next(key for key, value in self._shortPrint.items() if value == pieaceLetter.upper())
          firstPlayer = pieaceLetter.isupper()
          piece = Piece(firstPlayer, creature, 0)
          piecePosition = (piece, position)
          position = self._navigate(Direction.LEFT, position)
          self._board.append(piecePosition)
    
      
    self._playerOneTurn = playerOneTurn

  _shortPrint: Dict[Creatues, str] = {
        Creatues.Beetle: "B",
        Creatues.Grasshopper: "G",
        Creatues.QueenBee: "Q",
        Creatues.SoldierAnt: "A",
        Creatues.Spider: "S",
        Creatues.Mosquity: "M",
        Creatues.Ladybug: "L",        
  }

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
    return position.y*100+position.x