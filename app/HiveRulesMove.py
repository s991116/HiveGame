from typing import List
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Directions import Direction

class HiveRulesMove:

  def __init__(self, board: HiveBoard) -> None:
    self.board = board

  def addMovementMoves(self, moves: List[BoardPiece], playerOneTurn: bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return moves
    
    if(playerOneTurn):
        queenP1 = self.board.findPiece(self.board.pieces.QueenBeeP1)
        if queenP1 is not None:
          moves.append(queenP1.pieceToMove(Direction.UP_LEFT))

    if(not playerOneTurn):
        queenP2 = self.board.findPiece(self.board.pieces.QueenBeeP2)
        if queenP2 is not None:
          moves.append(queenP2.pieceToMove(Direction.UP_LEFT))

    return moves

  def moveablePieces(self, playerOneTurn:bool, queenPlaced: bool) -> List[BoardPiece]:
    if not queenPlaced:
      return []

    moveablePieces: List[BoardPiece] = []
    playerBoardPieces = self.board.getPlayerBoardPieces(playerOneTurn)
    for playerBoardPiece in playerBoardPieces:
      bridgingPieces = self.board.getBridgingPieces(playerBoardPiece)
      if bridgingPieces is None or not self.board.isConnectionBetweenPieces(bridgingPieces):
        moveablePieces.append(playerBoardPiece)

    return moveablePieces