import unittest
from app.HiveGame import HiveGame
from app.Coordinate import Coordinate
from app.HivePieces import HivePieces

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
        hivePieces = HivePieces()

        #Act
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, Coordinate(0,0)))

        #Assert
        board = hiveGame.getBoard()
        self.assertListEqual(board,[HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, Coordinate(0,0))])
        self.assertFalse(hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_two_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        hivePieces = HivePieces()

        #Act
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P2, Coordinate(-1,0)))

        #Assert
        board = hiveGame.getBoard()
        self.assertIn(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P1, Coordinate(0,0)), board)
        self.assertIn(HivePieces.CreateCloneWithCoordinate(hivePieces.Grasshopper_0_P2, Coordinate(-1,0)), board)

        self.assertTrue(hiveGame.rules.playerOneTurn) # type: ignore

    def test_init_board_with_three_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        playerOneTurn = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate( 0, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P2, Coordinate(-1, 0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_1_P1, Coordinate(+1, 0)))

        #Assert
        board = hiveGame.getBoard()
        pieceA = HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P1, Coordinate( 0,0))
        pieceC = HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_0_P2, Coordinate(-1,0))
        pieceB = HivePieces.CreateCloneWithCoordinate(pieces.Grasshopper_1_P1, Coordinate( 1,0))


        self.assertIn(pieceA, board)
        self.assertIn(pieceB, board)
        self.assertIn(pieceC, board)

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
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))

        #Assert
        freePiecesP1 = hiveGame.board.playableFreePieces(firstPlayer)
        self.assertEqual(len(freePiecesP1), 4)

    def test_free_pieces_after_Both_Qeen_and_AntP1_is_played(self):
        #Arrange
        hiveGame = HiveGame()
        firstPlayer = True
        pieces = hiveGame.board.pieces

        #Act
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate(1,0)))

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
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,0)))

        #Act
        move2 = hiveGame.getValidMoves()[0]
        hiveGame.playMove(move2)

        #Assert
        self.assertEqual(len(hiveGame.getBoard()), 2)

    def test_add_second_piece_for_P2(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate(0,1)))

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 15)

    def test_add_second_piece_for_P2_to_straght_line(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate(1,0)))

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
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Beetle_0_P1, Coordinate(0,0)))

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
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Beetle_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Beetle_0_P2, Coordinate(-1,0)))

#        hiveGame.setupPosition(["b0|B0"], True)

        #Act
        moves = hiveGame.getValidMoves()

        #Arrange
        self.assertEqual(len(moves), 10)

    def test_get_no_dublicate_move2_for_4_pieces_in_a_row(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate( 0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate( 1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P2, Coordinate(-2,0)))

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        self.assertEqual(len(moves), 3*5)

    def test_piece_updated_index_when_placing_same_creature(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate( 0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))

        #Act
        moves = hiveGame.getValidMoves()

        #Assert
        antWithNewIndex = HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate(1,0))
        self.assertIn(antWithNewIndex, moves)

    def test_piece_updated_index_when_placing_same_creature_after_Queen_is_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate( 0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1,    Coordinate( 1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2,    Coordinate(-2,0)))

        #Act
        moves = hiveGame.getValidMoves()
        print(hiveGame.board.printBoard())

        #Assert
        antWithNewIndex = HivePieces.CreateCloneWithCoordinate(pieces.Ant_1_P1, Coordinate(2,0))
        self.assertIn(antWithNewIndex, moves)

""" 
    def test_center_pieces_when_P1_Queen_is_played(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate(0,1)))

        #Act
        boardPieces = hiveGame.getBoard()

        #Assert
        self.assertIn(HivePieces.CreateCloneWithCoordinate(pieces.QueenBee_P1, Coordinate( 0, 0)),boardPieces)
        self.assertIn(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P1,    Coordinate(-1,-1)),boardPieces)
        self.assertIn(HivePieces.CreateCloneWithCoordinate(pieces.Ant_0_P2,    Coordinate(-2,-1)),boardPieces)
 """
if __name__ == "__main__":
    unittest.main()
