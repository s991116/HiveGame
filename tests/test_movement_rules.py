import unittest
from app.HiveGame import HiveGame
from app.BoardPiece import BoardPiece
from app.Coordinate import Coordinate

class TestMovmentRules(unittest.TestCase):

    def test_movement_not_possible_if_P1_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P1, Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP2, Coordinate(-1,0)))

        #Act
        movementMoves = hiveGame.rules.addMovementMoves([])

        #Arrange
        self.assertEqual(len(movementMoves), 0)


    def test_movement_not_possible_if_P2_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P1, Coordinate(1,0)))        

        #Act
        movementMoves = hiveGame.rules.addMovementMoves([])

        #Arrange
        self.assertEqual(len(movementMoves), 0)


    def test_movement_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP2, Coordinate(-1,0)))

        #Act
        movementMoves = hiveGame.rules.addMovementMoves([])

        #Arrange
        self.assertEqual(len(movementMoves), 1)

    def test_movement_for_P2_after_P2_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP2, Coordinate(-1,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P1, Coordinate(1,0)))        

        #Act
        movementMoves = hiveGame.rules.addMovementMoves([])

        #Arrange
        self.assertEqual(len(movementMoves), 1)



if __name__ == "__main__":
    unittest.main()
