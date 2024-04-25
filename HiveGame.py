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
    self._playerOneTurns = True

  def setPiece(self, move: Tuple[Piece, Position]):
    self._playerOneTurns = not self._playerOneTurns
    self._board.append(move)

  def getValidMoves(self) -> List[Tuple[Piece, Position]]:
    moves:list[Tuple[Piece, Position]] = []
    if(self._playerOneTurns):
      for piece in self.playerPieces:
        if(piece.firstPlayer == self._playerOneTurns and piece.index == 0):
          moves.append((piece, self.centerPosition))
    else:
      for piece in self.playerPieces:
        if(piece.firstPlayer == self._playerOneTurns and piece.index == 0):        
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
