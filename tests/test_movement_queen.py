import unittest
from app.Coordinate import Coordinate
from app.Species import Species
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentQueen(unittest.TestCase):

    def test_movement_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,  0, 0).\
            Play(HivePiece.QueenBee_P2, -1, 0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 2)
        self.assertEqual(movementMoves[0].piece.creature, Species.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Species.QueenBee)

    def test_movement_for_P2_after_P2_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.Ant_0_P1,  1, 0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 2)
        self.assertEqual(movementMoves[0].piece.creature, Species.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Species.QueenBee)

    def test_movement_for_Queen_with_multiple_connections_and_space(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.Ant_0_P1,  1, 0).\
            Play(HivePiece.Ant_0_P2, -2, 0).\
            Play(HivePiece.Ant_1_P1,  1, 1).\
            Play(HivePiece.Ant_1_P2, -3, 0).\
            Play(HivePiece.Ant_2_P1,  1, 2).\
            Play(HivePiece.Ant_2_P2, -2,-1).\
            Play(HivePiece.Grasshopper_0_P1, 0, 2).\
            Play(HivePiece.Grasshopper_0_P2,-1,-2).\
            Play(HivePiece.Grasshopper_1_P1,-1, 1).\
            Play(HivePiece.Grasshopper_1_P2, 0,-2).\
            Build()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.QueenBee_P1, Coordinate(0, -1)).Build()
        self.assertIn(move1, movementMoves)
        move2 = BoardPieceBuilder().WithHivePiece(HivePiece.QueenBee_P1, Coordinate(-1, -1)).Build()
        self.assertIn(move2, movementMoves)


if __name__ == "__main__":
    unittest.main()
