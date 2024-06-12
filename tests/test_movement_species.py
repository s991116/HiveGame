import unittest
from app.Coordinate import Coordinate
from app.Creatures import Creatures
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.HivePieceBuilder import HivePieceBuilder

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentSpecies(unittest.TestCase):

    def test_movement_grasshopper(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.SoldierAnt_0_P2, -1, 0).\
            Play(HivePiece.Grasshopper_0_P1, 1, 0).\
            Play(HivePiece.SoldierAnt_1_P2, -2, 0).\
            Play(HivePiece.SoldierAnt_1_P1,  0, 1).\
            Play(HivePiece.SoldierAnt_2_P2, -3, 0).\
            Build()
        pieces = hiveGame.board.pieces

        #Act
        g = hiveGame.board.findPiece(pieces.Grasshopper_0_P1.piece)
        if g is not None:
            grassHopperMoves = g.getMoves(hiveGame.board)
        else:
            grassHopperMoves = []

        print(hiveGame.board.printBoard())
        #Assert
        self.assertEqual(len(grassHopperMoves), 2)
        move1 = HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(-4,0))
        self.assertIn(move1, grassHopperMoves)
        move2 = HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(0,2))
        self.assertIn(move2, grassHopperMoves)


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
        self.assertEqual(movementMoves[0].piece.creature, Creatures.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Creatures.QueenBee)

    def test_movement_for_P2_after_P2_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.SoldierAnt_0_P1,  1, 0).\
            Build()

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 2)
        self.assertEqual(movementMoves[0].piece.creature, Creatures.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Creatures.QueenBee)

    def test_movement_for_Queen_with_multiple_connections_and_space(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0, 0).\
            Play(HivePiece.QueenBee_P2,     -1, 0).\
            Play(HivePiece.SoldierAnt_0_P1,  1, 0).\
            Play(HivePiece.SoldierAnt_0_P2, -2, 0).\
            Play(HivePiece.SoldierAnt_1_P1,  1, 1).\
            Play(HivePiece.SoldierAnt_1_P2, -3, 0).\
            Play(HivePiece.SoldierAnt_2_P1,  1, 2).\
            Play(HivePiece.SoldierAnt_2_P2, -2,-1).\
            Play(HivePiece.Grasshopper_0_P1, 0, 2).\
            Play(HivePiece.Grasshopper_0_P2,-1,-2).\
            Play(HivePiece.Grasshopper_1_P1,-1, 1).\
            Play(HivePiece.Grasshopper_1_P2, 0,-2).\
            Build()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0, -1))
        self.assertIn(move1, movementMoves)
        move2 = HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(-1, -1))
        self.assertIn(move2, movementMoves)


if __name__ == "__main__":
    unittest.main()
