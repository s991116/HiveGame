# test_my_module.py

import unittest
from HiveGame import HiveGame

class TestBasicRules(unittest.TestCase):

    def test_start_with_empty_board(self):
        
        #Arrange
        hiveGame = HiveGame()

        #Act
        board = hiveGame.getBoard()

        #Assert
        self.assertEqual(len(board), 0)

    def test_add_first_piece(self):
        
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.playerOnePieces
        onePiece = pieces[0]
        centerPosition = hiveGame.centerPosition

        #Act
        hiveGame.setPiece(onePiece, centerPosition)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 1)

    def test_add_second_piece(self):
        
        #Arrange
        hiveGame = HiveGame()
        piecesP1 = hiveGame.playerOnePieces
        onePieceP1 = piecesP1[0]
        centerPosition = hiveGame.centerPosition
        hiveGame.setPiece(onePieceP1, centerPosition)
        piecesP2 = hiveGame.playerTwoPieces
        onePieceP2 = piecesP2[0]
        centerPosition = hiveGame.centerPosition

        #Act
        hiveGame.setPiece(onePieceP2, centerPosition)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_get_valid_first_move_for_P1(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)


if __name__ == "__main__":
    unittest.main()
