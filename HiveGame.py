from typing import List
from Piece import Piece
from Creatues import Creatues
from Directions import Direction
from HiveBoard import HiveBoard
class HiveGame:

  def __init__(self) -> None:
    
    self.creatues: list[Creatues] = [
      Creatues.Beetle, 
      Creatues.Grasshopper, 
      Creatues.QueenBee, 
      Creatues.SoldierAnt, 
      Creatues.Spider]

    self.board = HiveBoard()
    self._playerOneTurn = True

  def playMove(self, move: Piece):
    self._playerOneTurn = not self._playerOneTurn
    self.board.setPiece(move)

  def getValidMoves(self) -> List[Piece]:
    moves:list[Piece] = []
    if(self._playerOneTurn):
      if(self.board.isEmpty()):
        for creature in self.creatues:
            moves.append(Piece(True, creature, 0, self.board.centerCoordinate))
      else:
        coordinates = [
                        self.board.navigate(Direction.UP_RIGHT, self.board.centerCoordinate),
                        self.board.navigate(Direction.RIGHT, self.board.centerCoordinate)]
        for coordinate in coordinates:
          for creature in self.creatues:
              moves.append(Piece(True, creature, 0, coordinate))

    else:
      for creature in self.creatues:
        moves.append(Piece(False, creature, 0, self.board.navigate(Direction.LEFT, self.board.centerCoordinate)))

    return moves
  
  def getBoard(self) -> List[Piece]:
    return self.board.getBoard()
  
  def setupPosition(self, boardPrint: str, playerOneTurn: bool):      
    self.board.setupPosition(boardPrint)
    self._playerOneTurn = playerOneTurn