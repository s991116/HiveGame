import unittest
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.PieceBuilder import PieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentSpider(unittest.TestCase):

    def test_movement_spider(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Ant_0_P2, -1, 0).\
            Play(HivePiece.Spider_0_P1, 1, 0).\
            Play(HivePiece.Ant_1_P2, -2, 0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        print(hiveGame.board.printBoard())

        #Assert
        spiderPiece = PieceBuilder().Spider_0_P1().Build()
        expectedMove1 = BoardPieceBuilder().WithPiece(spiderPiece).WithCoordinate(Coordinate(-2,1)).Build()
        self.assertIn(expectedMove1, movementMoves)
        expectedMove2 = BoardPieceBuilder().WithPiece(spiderPiece).WithCoordinate(Coordinate(-2,-1)).Build()
        self.assertIn(expectedMove2, movementMoves)

    def test_movement_for_Spider_in_a_ring_with_4_moves(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0,  0).\
            Play(HivePiece.QueenBee_P2,     -1,  0).\
            Play(HivePiece.Spider_0_P1,      1,  0).\
            Play(HivePiece.Ant_0_P2,        -2, -1).\
            Play(HivePiece.Spider_1_P1,      2,  0).\
            Play(HivePiece.Ant_1_P2,        -2, -2).\
            Play(HivePiece.Ant_0_P1,         2, -1).\
            Play(HivePiece.Ant_2_P2,        -2, -3).\
            Play(HivePiece.Ant_1_P1,         2, -2).\
            Play(HivePiece.Spider_0_P2,     -1, -3).\
            Play(HivePiece.Ant_2_P1,         1, -3).\
            Play(HivePiece.Spider_1_P2,      0, -3).\
            Build()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Spider_0_P1, Coordinate(-2,  1)).Build()
        self.assertIn(move1, movementMoves)
        move2 = BoardPieceBuilder().WithHivePiece(HivePiece.Spider_0_P1, Coordinate( 3,  0)).Build()
        self.assertIn(move2, movementMoves)
        move3 = BoardPieceBuilder().WithHivePiece(HivePiece.Spider_0_P1, Coordinate(-1, -2)).Build()
        self.assertIn(move3, movementMoves)
        move4 = BoardPieceBuilder().WithHivePiece(HivePiece.Spider_0_P1, Coordinate( 0, -2)).Build()
        self.assertIn(move4, movementMoves)

    def test_movement_for_Spider_into_sameplace(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0,  0).\
            Play(HivePiece.QueenBee_P2,     -1,  0).\
            Play(HivePiece.Spider_0_P1,      1,  0).\
            Play(HivePiece.Ant_0_P2,        -1, -1).\
            Play(HivePiece.Spider_1_P1,      2,  0).\
            Play(HivePiece.Ant_1_P2,         0, -2).\
            Play(HivePiece.Ant_0_P1,         2, -1).\
            Play(HivePiece.Ant_2_P2,         1, -2).\
            Play(HivePiece.Ant_1_P1,         2, -2).\
            Play(HivePiece.Spider_0_P2,     -1, -3).\
            Build()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Spider_0_P1, Coordinate(1, 0)).Build()
        self.assertNotIn(move1, movementMoves)



if __name__ == "__main__":
    unittest.main()
