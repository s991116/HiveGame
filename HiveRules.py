from typing import List
from HiveBoard import HiveBoard
from Piece import Piece
from Creatues import Creatues
from Directions import Direction
from Coordinate import Coordinate

class HiveRules:

  def __init__(self, board: HiveBoard) -> None:
    self.playerOneTurn = True
    self.board = board
    self.QueenP1Placed = False
    self.QueenP2Placed = False

    self.creatues: list[Creatues] = [
      Creatues.Beetle, 
      Creatues.Grasshopper, 
      Creatues.QueenBee, 
      Creatues.SoldierAnt, 
      Creatues.Spider]

  def playMove(self, move: Piece):  
    
    if(move.creature == Creatues.QueenBee):
      if(self.playerOneTurn):
        self.QueenP1Placed = True
      else:
        self.QueenP2Placed = True

    self.board.setPiece(move)
    self.playerOneTurn = not self.playerOneTurn

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
          for p in self.board.PlayablePieces(self.playerOneTurn):
              moves.append(Piece(self.playerOneTurn, p.creature, p.index, coordinate))
        if(self.QueenP1Placed):
          Q1P1 = Piece(True, Creatues.QueenBee, 0, Coordinate(0,0))
          moves.append(self.board.findPiece(Q1P1)[0].pieceToMove(Direction.UP_LEFT))
    else:
      for creature in self.creatues:
        moves.append(Piece(False, creature, 0, self.board.navigate(Direction.LEFT, self.board.centerCoordinate)))

    return moves
  
  def updatePosition(self):
    Q1P1 = Piece(True, Creatues.QueenBee, 0, Coordinate(0,0))
    Q1P2 = Piece(False, Creatues.QueenBee, 0, Coordinate(0,0))

    if(len(self.board.findPiece(Q1P1)) > 0):
      self.QueenP1Placed = True

    if(len(self.board.findPiece(Q1P2)) > 0):
      self.QueenP2Placed = True      