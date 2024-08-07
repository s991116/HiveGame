import unittest
from app.Coordinate import Coordinate
from app.HivePiece import HivePiece
from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.BoardPieceBuilder import BoardPieceBuilder
from app.Species import Species

class TestMovmentBeetle(unittest.TestCase):

    def createPiecesInARing(self):
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0,  0).\
            Play(HivePiece.QueenBee_P2,     -1,  0).\
            Play(HivePiece.Beetle_0_P1,      1,  0).\
            Play(HivePiece.Ant_0_P2,        -2, -1).\
            Play(HivePiece.Ant_0_P1,         2,  0).\
            Play(HivePiece.Ant_1_P2,        -1, -2).\
            Play(HivePiece.Ant_1_P1,         2, -1).\
            Play(HivePiece.Ant_2_P2,        -0, -2).\
            Play(HivePiece.Ant_2_P1,         2, -2).\
            Play(HivePiece.Spider_0_P2,      1, -2).\
            Build()
        return hiveGame
    
    def test_movement_for_Beetle_along_edge(self):
        #Arrange
        hiveGame = self.createPiecesInARing()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 0, 1)).Build()
        self.assertIn(move1, movementMoves)
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 1, 1)).Build()
        self.assertIn(move1, movementMoves)
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 0,-1)).Build()
        self.assertIn(move1, movementMoves)
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 1,-1)).Build()
        self.assertIn(move1, movementMoves)

    def test_possible_to_move_Beetle_on_top(self):
        #Arrange
        hiveGame = self.createPiecesInARing()

        print(hiveGame.board.printBoard())

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 0, 0)).Layer(1).Build()
        self.assertIn(move1, movementMoves)
        move1 = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate( 2, 0)).Layer(1).Build()
        self.assertIn(move1, movementMoves)

    def test_move_Beetle_on_top(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0,  0).\
            Play(HivePiece.QueenBee_P2,     -1,  0).\
            Play(HivePiece.Beetle_0_P1,      1,  0).\
            Play(HivePiece.Ant_0_P2,        -2, -1).\
            Build()

        #Act
        movedBeetle = BoardPieceBuilder().WithHivePiece(HivePiece.Beetle_0_P1, Coordinate(0, 0))
        hiveGame.playMove(movedBeetle.Build())

        #Assert
        boardPieces = hiveGame.getBoard()
        self.assertIn(movedBeetle.Layer(1).Build(), boardPieces)

    def test_piece_under_Beetle_cannot_move(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,      0,  0).\
            Play(HivePiece.QueenBee_P2,     -1,  0).\
            Play(HivePiece.Beetle_0_P1,      1,  0).\
            Play(HivePiece.Ant_0_P2,        -2, -1).\
            Play(HivePiece.Beetle_0_P1,      0,  0).\
            Play(HivePiece.Ant_1_P2,        -2, -1).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()
        
        #Assert
        for move in moves:
            self.assertNotEqual(move.piece.creature, Species.QueenBee)


if __name__ == "__main__":
    unittest.main()
