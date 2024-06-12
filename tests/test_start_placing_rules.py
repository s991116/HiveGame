import unittest
from app.HiveGame import HiveGame
from app.Coordinate import Coordinate

from tests.HiveGameTestBuilder import HiveGameTestBuilder
from app.HivePieceBuilder import HivePieceBuilder
from app.HivePiece import HivePiece
class TestStartPlacingRules(unittest.TestCase):

    def test_start_with_empty_board(self):        
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()

        #Act
        board = hiveGame.getBoard()

        #Assert
        self.assertEqual(len(board), 0)

    def test_init_board_with_one_piece(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()

        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(0,0)))

        #Assert
        board = hiveGame.getBoard()
        self.assertListEqual(board,[HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(0,0))])
        self.assertFalse(hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_two_pieces(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()

        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P2, Coordinate(-1,0)))

        #Assert
        board = hiveGame.getBoard()
        self.assertIn(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate(0,0)), board)
        self.assertIn(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P2, Coordinate(-1,0)), board)

        self.assertTrue(hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_three_pieces(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()
        
        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate( 0,0)))
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.Grasshopper_1_P1, Coordinate( 1,0)))

        #Assert
        board = hiveGame.getBoard()
        pieceA = HivePieceBuilder().Build(HivePiece.Grasshopper_0_P1, Coordinate( 0,0))
        pieceC = HivePieceBuilder().Build(HivePiece.Grasshopper_0_P2, Coordinate(-1,0))
        pieceB = HivePieceBuilder().Build(HivePiece.Grasshopper_1_P1, Coordinate( 1,0))

        self.assertIn(pieceA, board)
        self.assertIn(pieceB, board)
        self.assertIn(pieceC, board)
        self.assertFalse(hiveGame.rules.playerOneTurn) # type: ignore

    def test_free_pieces_when_game_starts(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()

        #Act
        firstPlayer = True
        freePiecesP1 = hiveGame.board.playableFreePieces(firstPlayer)

        firstPlayer = False
        freePiecesP2 = hiveGame.board.playableFreePieces(firstPlayer)

        #Assert
        self.assertEqual(len(freePiecesP1), 5)
        self.assertEqual(len(freePiecesP2), 5)

    def test_free_pieces_after_QeenBeeP1_is_played(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()

        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,0)))

        #Assert
        firstPlayer = True
        freePiecesP1 = hiveGame.board.playableFreePieces(firstPlayer)
        self.assertEqual(len(freePiecesP1), 4)

    def test_free_pieces_after_Both_Qeen_and_AntP1_is_played(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Build()
        firstPlayer = True

        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.QueenBee_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.SoldierAnt_0_P1, Coordinate(1,0)))

        #Assert
        freePiecesP1 = hiveGame.board.playableFreePieces(firstPlayer)
        self.assertEqual(len(freePiecesP1), 4)
        freePiecesP2 = hiveGame.board.playableFreePieces(firstPlayer)
        self.assertEqual(len(freePiecesP2), 4)

    def test_add_first_piece(self):        
        #Arrange
        hiveGame = HiveGame()
        move = hiveGame.getValidMoves()[0]

        #Act
        hiveGame.playMove(move)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 1)

    def test_add_second_piece(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1, 0, 0).\
            Build()

        #Act
        move2 = hiveGame.getValidMoves()[0]
        hiveGame.playMove(move2)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_add_second_piece_for_P2(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.SoldierAnt_0_P1, 0, 0).\
            Play(HivePiece.SoldierAnt_0_P2,-1, 0).\
            Play(HivePiece.SoldierAnt_1_P1, 0, 1).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 15)

    def test_add_second_piece_for_P2_to_straght_line(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.SoldierAnt_0_P1, 0, 0).\
            Play(HivePiece.SoldierAnt_0_P2,-1, 0).\
            Play(HivePiece.SoldierAnt_1_P1, 1, 0).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 10)

    def test_get_valid_first_move_for_P1(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for boardPiece in moves:
          self.assertTrue(boardPiece.piece.firstPlayer)
          self.assertEqual(boardPiece.coordinate, hiveGame.board.centerCoordinate)

    def test_get_valid_first_move_for_P2(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.Beetle_0_P1, 0,0).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for boardPiece in moves:
            self.assertFalse(boardPiece.piece.firstPlayer)
            self.assertNotEqual(boardPiece.coordinate, hiveGame.board.centerCoordinate)

    def test_get_valid_second_move_for_P1_Queen_Not_Played(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.Beetle_0_P1, 0,0).\
            Play(HivePiece.Beetle_0_P2, -1,0).\
            Build()
        
        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 10)

    def test_get_no_dublicate_move2_for_4_pieces_in_a_row(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.SoldierAnt_0_P1, 0,0).\
            Play(HivePiece.SoldierAnt_0_P2,-1,0).\
            Play(HivePiece.SoldierAnt_1_P1, 1,0).\
            Play(HivePiece.SoldierAnt_1_P2, -2,0).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 3*5)

    def test_piece_updated_index_when_placing_same_creature(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.SoldierAnt_0_P1, 0,0).\
            Play(HivePiece.SoldierAnt_0_P2,-1,0).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        antWithNewIndex = HivePieceBuilder().Build(HivePiece.SoldierAnt_1_P1, Coordinate(1,0))
        self.assertIn(antWithNewIndex, moves)

    def test_piece_updated_index_when_placing_same_creature_after_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.QueenBee_P1,     0,0).\
            Play(HivePiece.QueenBee_P2,    -1,0).\
            Play(HivePiece.SoldierAnt_0_P1, 1,0).\
            Play(HivePiece.SoldierAnt_0_P2,-2,0).\
            Build()

        #Act
        moves = hiveGame.getValidMoves()
        print(hiveGame.board.printBoard())

        #Assert
        antWithNewIndex = HivePieceBuilder().Build(HivePiece.SoldierAnt_1_P1, Coordinate(2,0))
        self.assertIn(antWithNewIndex, moves)

    def test_center_pieces_when_P1_Queen_is_played(self):
        #Arrange
        hiveGame = HiveGameTestBuilder().\
            Play(HivePiece.SoldierAnt_0_P1,  0,0).\
            Play(HivePiece.SoldierAnt_0_P2, -1,0).\
            Build()

        #Act
        hiveGame.playMove(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,1)))

        #Assert
        boardPieces = hiveGame.getBoard()
        self.assertIn(HivePieceBuilder().Build(HivePiece.QueenBee_P1, Coordinate(0,0)),boardPieces)
        self.assertIn(HivePieceBuilder().Build(HivePiece.SoldierAnt_0_P1, Coordinate(-1,-1)),boardPieces)
        self.assertIn(HivePieceBuilder().Build(HivePiece.SoldierAnt_0_P2, Coordinate(-2,-1)),boardPieces)
 
if __name__ == "__main__":
    unittest.main()
