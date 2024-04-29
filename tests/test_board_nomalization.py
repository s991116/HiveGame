import unittest
from app.HiveBoard import HiveBoard
from app.Creatues import Creatues
from app.Coordinate import Coordinate

class TestBoardNomalization(unittest.TestCase):

    def test_center_P1_QueenBee(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setupPosition("A0|a0|Q0")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece in board:
            if(piece.creature == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(piece.coordinate, Coordinate(0,0))
        
    def test_center_P1_QueenBee_PlacedFirst(self):
        #Arrange
        hiveBoard = HiveBoard()

        #Act
        hiveBoard.setupPosition("A0|Q0|a0")        

        #Assert
        board = hiveBoard.getBoard()
        
        self.assertEqual(len(board), 3)
        for piece in board:
            if(piece.creature == Creatues.QueenBee and piece.firstPlayer):
                self.assertEqual(piece.coordinate, Coordinate(0,0))

if __name__ == "__main__":
    unittest.main()
