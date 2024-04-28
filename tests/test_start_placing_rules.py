import unittest
from HiveGame import HiveGame
from Piece import Piece
from Creatues import Creatues
from Coordinate import Coordinate

class TestStartPlacingRules(unittest.TestCase):

    def test_start_with_empty_board(self):
        
        #Arrange
        hiveGame = HiveGame()

        #Act
        board = hiveGame.getBoard()

        #Assert
        self.assertEqual(len(board), 0)

    def test_init_board_with_one_piece(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = False
        #Act
        hiveGame.setupPosition("Q0", playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        self.assertListEqual(board,[Piece(True,Creatues.QueenBee, 0, Coordinate(0,0))])
        self.assertEqual(playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_two_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = True
        #Act
        hiveGame.setupPosition("q0|Q0", playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        pieceA = Piece(True,Creatues.QueenBee, 0, Coordinate(0,0))
        pieceB = Piece(False,Creatues.QueenBee, 0, Coordinate(-1,0))
        self.assertListEqual(board,[pieceA, pieceB])
        self.assertEqual(playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_three_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = True
        #Act
        hiveGame.setupPosition("q0|Q0|A0", not playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        pieceA = Piece(True,Creatues.SoldierAnt, 0, Coordinate(1,0))
        pieceB = Piece(True,Creatues.QueenBee, 0, Coordinate(0,0))
        pieceC = Piece(False,Creatues.QueenBee, 0, Coordinate(-1,0))


        self.assertListEqual(board,[pieceA, pieceB, pieceC])
        self.assertEqual(not playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore


    def test_free_pieces_when_game_starts(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        firstPlayer = True
        freePiecesP1 = hiveGame.board.freePieces(firstPlayer)

        firstPlayer = False
        freePiecesP2 = hiveGame.board.freePieces(firstPlayer)

        #Assert
        self.assertEqual(len(freePiecesP1), 11)
        self.assertEqual(len(freePiecesP2), 11)

    def test_free_pieces_after_first_piece_is_played(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        firstPlayer = True
        hiveGame.playMove(hiveGame.getValidMoves()[0])
        freePiecesP1 = hiveGame.board.freePieces(firstPlayer)

        #Assert
        self.assertEqual(len(freePiecesP1), 10)

    def test_free_pieces_after_three_piece_is_played(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        firstPlayer = True

        for _ in [0,1,2]:
            hiveGame.playMove(hiveGame.getValidMoves()[0])
        freePiecesP1 = hiveGame.board.freePieces(firstPlayer)
        freePiecesP2 = hiveGame.board.freePieces(not firstPlayer)

        #Assert
        self.assertEqual(len(freePiecesP1), 9)
        self.assertEqual(len(freePiecesP2), 10)

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
        hiveGame = HiveGame()
        hiveGame.setupPosition("Q0", False)

        #Act
        move2 = hiveGame.getValidMoves()[0]
        hiveGame.playMove(move2)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_get_valid_first_move_for_P1(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for piece in moves:
          self.assertTrue(piece.firstPlayer)
          self.assertEqual(piece.coordinate, hiveGame.board.centerCoordinate)

    def test_get_valid_first_move_for_P2(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition("B0", False)

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for piece in moves:
            self.assertFalse(piece.firstPlayer)
            self.assertNotEqual(piece.coordinate, hiveGame.board.centerCoordinate)

    def test_get_valid_second_move_for_P1_Queen_Not_Played(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition("b0|B0", True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 10)

    def test_move_piece_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition("b0|Q0", True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 9)



if __name__ == "__main__":
    unittest.main()
