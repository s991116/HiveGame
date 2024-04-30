import unittest
from app.HiveGame import HiveGame
from app.BoardPiece import BoardPiece
from app.Coordinate import Coordinate

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
        pieces = hiveGame.board.pieces
        playerOneTurn = False

        #Act
        hiveGame.setupPosition(["Q0"], playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        self.assertListEqual(board,[BoardPiece(pieces.QueenBeeP1, Coordinate(0,0))])
        self.assertEqual(playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_two_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.setupPosition(["q0|Q0"], playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        pieceA = BoardPiece(pieces.QueenBeeP1, Coordinate(0,0))
        pieceB = BoardPiece(pieces.QueenBeeP2, Coordinate(-1,0))
        self.assertListEqual(board,[pieceA, pieceB])
        self.assertEqual(playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_three_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.setupPosition(["q0|Q0|A0"], not playerOneTurn)

        #Assert
        board = hiveGame.getBoard()
        pieceA = BoardPiece(pieces.Ant_0_P1, Coordinate(1,0))
        pieceB = BoardPiece(pieces.QueenBeeP1, Coordinate(0,0))
        pieceC = BoardPiece(pieces.QueenBeeP2, Coordinate(-1,0))


        self.assertListEqual(board,[pieceA, pieceB, pieceC])
        self.assertEqual(not playerOneTurn, hiveGame.rules.playerOneTurn) # type: ignore


    def test_free_pieces_when_game_starts(self):
        #Arrange
        hiveGame = HiveGame()

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
        hiveGame = HiveGame()
        firstPlayer = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))

        #Assert
        freePiecesP1 = hiveGame.board.playableFreePieces(firstPlayer)
        self.assertEqual(len(freePiecesP1), 4)

    def test_free_pieces_after_Both_Qeen_and_AntP1_is_played(self):
        #Arrange
        hiveGame = HiveGame()
        firstPlayer = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1,Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP2,Coordinate(-1,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P1,Coordinate(1,0)))

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
        hiveGame = HiveGame()
        hiveGame.setupPosition(["Q0"], False)

        #Act
        move2 = hiveGame.getValidMoves()[0]
        hiveGame.playMove(move2)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_add_second_piece_for_P2(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(BoardPiece(pieces.Ant_0_P1, Coordinate(0,1)))

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 12)


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
        hiveGame = HiveGame()
        hiveGame.setupPosition(["B0"], False)

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for boardPiece in moves:
            self.assertFalse(boardPiece.piece.firstPlayer)
            self.assertNotEqual(boardPiece.coordinate, hiveGame.board.centerCoordinate)

    def test_get_valid_second_move_for_P1_Queen_Not_Played(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition(["b0|B0"], True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 10)

    def test_move_piece_after_P1_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        hiveGame.setupPosition(["b0|Q0"], True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 9)



if __name__ == "__main__":
    unittest.main()
