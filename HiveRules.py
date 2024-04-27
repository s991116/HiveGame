from typing import List
from HiveBoard import HiveBoard
from Piece import Piece
from Creatues import Creatues
from Directions import Direction

class HiveRules:

  def __init__(self, board: HiveBoard) -> None:
    self.playerOneTurn = True
    self.board = board

    self.creatues: list[Creatues] = [
      Creatues.Beetle, 
      Creatues.Grasshopper, 
      Creatues.QueenBee, 
      Creatues.SoldierAnt, 
      Creatues.Spider]

  def playMove(self, move: Piece):  
    self._playerOneTurn = not self.playerOneTurn
    self.board.setPiece(move)

  def getValidMoves(self) -> List[Piece]:
    moves:list[Piece] = []
    if(self.playerOneTurn):
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
