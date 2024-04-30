import unittest
from app.HiveBoard import HiveBoard
from app.Creatues import Creatues
from app.Coordinate import Coordinate
from app.BoardPiece import BoardPiece

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        hiveBoard = HiveBoard()
        pieces = hiveBoard.pieces

        #Act
        hiveBoard.movePiece(BoardPiece(pieces.Spider_0_P1, Coordinate(0,0)))
        hiveBoard.movePiece(BoardPiece(pieces.Spider_0_P2, Coordinate(-1,0)))
        hiveBoard.movePiece(BoardPiece(pieces.QueenBeeP1, Coordinate(+1,0)))

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for boardPiece in board:
            if(boardPiece.piece.creature == Creatues.QueenBee and boardPiece.piece.firstPlayer):
                self.assertEqual(boardPiece.coordinate, Coordinate(0,0))
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        hiveBoard = HiveBoard()
        pieces = hiveBoard.pieces

        #Act
        hiveBoard.movePiece(BoardPiece(pieces.QueenBeeP1, Coordinate(0,0)))
        hiveBoard.movePiece(BoardPiece(pieces.Spider_0_P2, Coordinate(-1,0)))
        hiveBoard.movePiece(BoardPiece(pieces.Spider_0_P1, Coordinate(+1,0)))

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for boardPiece in board:
            if(boardPiece.piece.creature == Creatues.QueenBee and boardPiece.piece.firstPlayer):
                self.assertEqual(boardPiece.coordinate, Coordinate(0,0))

    # def test_center_Rotate_P2_QueenBee(self):
    #     #Arrange
    #     #Arrange
    #     hiveBoard = HiveBoard()
    #     hiveBoard.movePiece(Piece(True, Creatues.QueenBee, 0, Coordinate(0,0)))
    #     hiveBoard.movePiece(Piece(False, Creatues.Spider, 0, Coordinate(-1,0)))
    #     hiveBoard.movePiece(Piece(True, Creatues.Spider, 0, Coordinate(+1,0)))

    #     #Act
    #     hiveBoard.movePiece(Piece(False, Creatues.QueenBee, 0, Coordinate(-1,1)))

    #     #Assert
    #     hiveBoard.findPiece(Piece(True, Creatues.QueenBee, 0, ))

if __name__ == "__main__":
    unittest.main()
