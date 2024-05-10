from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.HivePieces import HivePieces
from app.Creatures import Creatures
from app.Directions import Direction
from app.HiveRulesMove import HiveRulesMove
from app.HiveRulesPlacement import HiveRulesPlacement

class HiveRules:

  def __init__(self, board: HiveBoard) -> None:
    self.playerOneTurn = True
    self.board = board
    self.QueenP1Placed = False
    self.QueenP2Placed = False
    self.hiveRulesMove = HiveRulesMove(self.board)
    self.hiveRulesPlacement = HiveRulesPlacement(self.board)

  def playMove(self, move: BoardPiece):  
    
    if(move.piece.creature == Creatures.QueenBee):
      if(self.playerOneTurn):
        self.QueenP1Placed = True
      else:
        self.QueenP2Placed = True

    self.board.movePiece(move)
    self.playerOneTurn = not self.playerOneTurn

  def getValidMoves(self) -> List[BoardPiece]:

    moves:list[BoardPiece] = []

    if(len(self.board.getBoard())<=1):
      if(self.playerOneTurn):
        startPosition = self.board.centerCoordinate
      else:
        startPosition = self.board.navigate(Direction.LEFT, self.board.centerCoordinate)
        
      for playablePiece in self.board.playableFreePieces(self.playerOneTurn):
        moves.append(HivePieces.CreateCloneWithCoordinate(playablePiece, startPosition))
      return moves

    moves += self.hiveRulesPlacement.getPlacementMoves(self.playerOneTurn)
    moves += self.getMovementMoves()
    return moves    

  def moveablePieces(self) -> List[BoardPiece]:
    queenPlaced = self.isQueenPlaced()
    return self.hiveRulesMove.moveablePieces(self.playerOneTurn, queenPlaced)

  def getMovementMoves(self):
    queenPlaced = self.isQueenPlaced()
    moves = self.hiveRulesMove.getMovementMoves(self.playerOneTurn, queenPlaced)
    return moves

  def isQueenPlaced(self) -> bool:
    return (self.playerOneTurn and self.QueenP1Placed) or (not self.playerOneTurn and self.QueenP2Placed)

  def updatePosition(self):
    Q1P1 = self.board.pieces.QueenBee_P1
    Q1P2 = self.board.pieces.QueenBee_P2

    if self.board.findPiece(Q1P1.piece) is not None:
      self.QueenP1Placed = True

    if self.board.findPiece(Q1P2.piece) is not None:
      self.QueenP2Placed = True      