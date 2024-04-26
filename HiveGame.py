from typing import List, Tuple, Dict
from Piece import Piece
from Creatues import Creatues
from Position import Position
from Directions import Direction
from HiveBoard import HiveBoard
class HiveGame:

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

    self.board = HiveBoard()
    self._playerOneTurn = True

  def move(self, move: Tuple[Piece, Position]):
    self._playerOneTurn = not self._playerOneTurn
    self.board.setPiece(move)

  def getValidMoves(self) -> List[Tuple[Piece, Position]]:
    moves:list[Tuple[Piece, Position]] = []
    if(self._playerOneTurn):
      if(self.board.isEmpty()):
        for piece in self.playerPieces:
          if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):
            moves.append((piece, Position(self.board.getCenterCoordinate())))
      else:
        positions = [self.board.navigate(Direction.UP_RIGHT, Position(self.board.getCenterCoordinate())), self.board.navigate(Direction.RIGHT, Position(self.board.getCenterCoordinate()))]
        for position in positions:
          for piece in self.playerPieces:
            if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):
              moves.append((piece, position))

    else:
      for piece in self.playerPieces:
        if(piece.firstPlayer == self._playerOneTurn and piece.index == 0):        
          moves.append((piece, self.board.navigate(Direction.LEFT, Position(self.board.getCenterCoordinate()))))

    return moves
  
  def getPlayerPieces(self, playerOne:bool) -> List[Piece]:
    pieces: list[Piece] = []
    for piece in self.playerPieces:
      if(piece.firstPlayer == playerOne and piece.index == 0):
        pieces.append(piece)
    return pieces

  def getBoard(self) -> List[Tuple[Piece, Position]]:    
    return self.board.getBoard()
  
  def moveLeft(self) -> None:
    self.x = self.x-1

  def setPosition(self, boardPrint: str, playerOneTurn: bool):      
    self.board.setPosition(boardPrint)
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