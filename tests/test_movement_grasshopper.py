import unittest
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.PieceBuilder import PieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentGrasshopper(unittest.TestCase):

    def test_movement_grasshopper(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.Ant_0_P2, -1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Play(HivePiece.Ant_1_P2, -2, 0).\
            Play(HivePiece.Ant_1_P1,  0, 1).\
            Play(HivePiece.Ant_2_P2, -3, 0).\
            Build()

        #Act
        g = hiveGame.board.findPiece(PieceBuilder().Grasshopper_0_P1().Build())
        if g is not None:
            grassHopperMoves = g.getMoves(hiveGame.board)
        else:
            grassHopperMoves = []

        print(hiveGame.board.printBoard())
        #Assert
        self.assertEqual(len(grassHopperMoves), 2)
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Grasshopper_0_P1, Coordinate(-4,0)).Build()
        self.assertIn(move1, grassHopperMoves)
        move2 = BoardPieceBuilder().WithHivePiece(HivePiece.Grasshopper_0_P1, Coordinate(0,2)).Build()
        self.assertIn(move2, grassHopperMoves)


if __name__ == "__main__":
    unittest.main()
