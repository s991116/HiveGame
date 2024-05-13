import unittest
from app.HiveGame import HiveGame
from app.Coordinate import Coordinate
from app.Creatures import Creatures
from app.HivePieces import HivePieces

param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentSpecies(unittest.TestCase):

    def test_movement_grasshopper(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces

        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate(1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-2,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate(0,1)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P2, Coordinate(-3,0)))

        #Act
        g = hiveGame.board.findPiece(pieces.Grasshopper_0_P1.piece)
        if g is not None:
            grassHopperMoves = g.getMoves(hiveGame.board)
        else:
            grassHopperMoves = []

        #Assert
        self.assertEqual(len(grassHopperMoves), 2)
        move1 = HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate(-4,0))
        self.assertIn(move1, grassHopperMoves)
        move2 = HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate(0,2))
        self.assertIn(move2, grassHopperMoves)


    def test_movement_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P2, Coordinate(-1,0)))

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 2)
        self.assertEqual(movementMoves[0].piece.creature, Creatures.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Creatures.QueenBee)

    def test_movement_for_P2_after_P2_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate(1,0)))        

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 2)
        self.assertEqual(movementMoves[0].piece.creature, Creatures.QueenBee)
        self.assertEqual(movementMoves[1].piece.creature, Creatures.QueenBee)

    def test_movement_for_Queen_with_multiple_connections_and_space(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1,      Coordinate( 0, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P2,      Coordinate(-1, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1,         Coordinate( 1, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2,         Coordinate(-2, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1,         Coordinate( 1, 1)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P2,         Coordinate(-3, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_2_P1,         Coordinate( 1, 2)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_2_P2,         Coordinate(-2,-1)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate( 0, 2)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P2, Coordinate(-1,-2)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_1_P1, Coordinate(-1, 1)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_1_P2, Coordinate( 0,-2)))

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,-1))
        self.assertIn(move1, movementMoves)
        move2 = HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(-1,-1))
        self.assertIn(move2, movementMoves)


if __name__ == "__main__":
    unittest.main()
