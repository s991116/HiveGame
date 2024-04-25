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
        piecesP1 = hiveGame.playerOnePieces
        move = (piecesP1[0],hiveGame.centerPosition)

        #Act
        hiveGame.setPiece(move)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 1)

    def test_add_second_piece(self):
        
        #Arrange
        hiveGame = HiveGame()
        piecesP1 = hiveGame.playerOnePieces
        move1 = (piecesP1[0],hiveGame.centerPosition)
        hiveGame.setPiece(move1)
        
        piecesP2 = hiveGame.playerTwoPieces
        move2 = (piecesP2[0],hiveGame.centerPosition)

        #Act
        hiveGame.setPiece(move2)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_get_valid_first_move_for_P1(self):
        #Arrange
        hiveGame = HiveGame()

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for (piece, _) in moves:
          self.assertTrue(piece.firstPlayer)


    def test_get_valid_first_move_for_P2(self):
        #Arrange
        hiveGame = HiveGame()
        moves = hiveGame.getValidMoves()
        hiveGame.setPiece(hiveGame.getValidMoves()[0])

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 5)
        for (piece, _) in moves:
            self.assertFalse(piece.firstPlayer)



if __name__ == "__main__":
    unittest.main()
