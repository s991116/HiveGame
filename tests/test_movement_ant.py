import unittest
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.PieceBuilder import PieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentAnt(unittest.TestCase):

    def test_movement_ant(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,   0, 0).\
            Play(HivePiece.Ant_0_P2,     -1, 0).\
            Play(HivePiece.Ant_0_P1,      1, 0).\
            Play(HivePiece.Ant_1_P2,     -2, 0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()
        print(hiveGame.board.printBoard())

        #Assert
        antPiece = PieceBuilder().Ant_0_P1().Build()
        expectedMove1 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate( 0, 1)).Build()
        self.assertIn(expectedMove1, movementMoves)
        expectedMove2 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-1, 1)).Build()
        self.assertIn(expectedMove2, movementMoves)
        expectedMove3 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-2, 1)).Build()
        self.assertIn(expectedMove3, movementMoves)
        expectedMove4 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-3, 1)).Build()
        self.assertIn(expectedMove4, movementMoves)
        expectedMove5 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-3, 0)).Build()
        self.assertIn(expectedMove5, movementMoves)
        expectedMove6 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-3,-1)).Build()
        self.assertIn(expectedMove6, movementMoves)
        expectedMove7 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-2,-1)).Build()
        self.assertIn(expectedMove7, movementMoves)
        expectedMove8 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-1,-1)).Build()
        self.assertIn(expectedMove8, movementMoves)
        expectedMove9 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate( 0,-1)).Build()
        self.assertIn(expectedMove9, movementMoves)

    def test_movement_ant_in_circle(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,   0, 0).\
            Play(HivePiece.Ant_0_P2,     -1, 0).\
            Play(HivePiece.Ant_0_P1,      1, 0).\
            Play(HivePiece.Ant_1_P2,     -2,-1).\
            Play(HivePiece.Ant_1_P1,      2, 0).\
            Play(HivePiece.Ant_2_P2,     -1,-2).\
            Play(HivePiece.Ant_2_P1,      2,-1).\
            Play(HivePiece.Spider_0_P2,   0,-2).\
            Play(HivePiece.Spider_0_P1,   2,-2).\
            Play(HivePiece.Spider_1_P2,   1,-2).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()
        print(hiveGame.board.printBoard())

        #Assert
        antPiece = PieceBuilder().Ant_0_P1().Build()
        expectedMove1 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate( 1,-1)).Build()
        self.assertIn(expectedMove1, movementMoves)
        expectedMove1 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate( 0,-1)).Build()
        self.assertIn(expectedMove1, movementMoves)
        expectedMove1 = BoardPieceBuilder().WithPiece(antPiece).WithCoordinate(Coordinate(-1,-1)).Build()
        self.assertNotIn(expectedMove1, movementMoves)

if __name__ == "__main__":
    unittest.main()
