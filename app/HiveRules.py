from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatues import Creatues
from app.Directions import Direction

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

  def playMove(self, move: BoardPiece):  
    
    if(move.piece.creature == Creatues.QueenBee):
      if(self.playerOneTurn):
        self.QueenP1Placed = True
      else:
        self.QueenP2Placed = True

    self.board.setPiece(move)
    self.playerOneTurn = not self.playerOneTurn

  def getValidMoves(self) -> List[BoardPiece]:
    moves:list[BoardPiece] = []
    if(self.playerOneTurn):
      if(self.board.isEmpty()):
        for creature in self.creatues:
            moves.append(BoardPiece(Piece(True, creature, 0), self.board.centerCoordinate))
      else:
        coordinates = [
                        self.board.navigate(Direction.UP_RIGHT, self.board.centerCoordinate),
                        self.board.navigate(Direction.RIGHT, self.board.centerCoordinate)]
        for coordinate in coordinates:
          for p in self.board.playableFreePieces(self.playerOneTurn):
              moves.append(BoardPiece(Piece(self.playerOneTurn, p.creature, p.index), coordinate))
        if(self.QueenP1Placed):
          Q1P1 = self.board.pieces.QueenBeeP1
          moves.append(self.board.findPiece(Q1P1)[0].pieceToMove(Direction.UP_LEFT))
    else:
      for creature in self.creatues:
        moves.append(BoardPiece(Piece(False, creature, 0), self.board.navigate(Direction.LEFT, self.board.centerCoordinate)))

    return moves
  
  def updatePosition(self):
    Q1P1 = self.board.pieces.QueenBeeP1
    Q1P2 = self.board.pieces.QueenBeeP2

    if(len(self.board.findPiece(Q1P1)) > 0):
      self.QueenP1Placed = True

    if(len(self.board.findPiece(Q1P2)) > 0):
      self.QueenP2Placed = True      