import unittest
from app.HiveBoard import HiveBoard

class TestPrintBoard(unittest.TestCase):

    def test_printBoard_dont_give_exception(self):
        #Arrange
        hiveBoard = HiveBoard()
        hiveBoard.setupPosition("A0|a0|Q0")        

        #Act
        hiveBoard.printBoard()

        #Assert
        
if __name__ == "__main__":
    unittest.main()
