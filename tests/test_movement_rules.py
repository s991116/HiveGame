import unittest
from typing import List, Tuple, Optional
from parameterized import parameterized # type: ignore
from app.HiveGame import HiveGame
from app.HiveBoard import HiveBoard
from app.BoardPiece import BoardPiece
from app.Piece import Piece
from app.Creatures import Creatures
from app.Coordinate import Coordinate
from app.Directions import Direction
from app.HiveRulesMove import HiveRulesMove
from app.HivePieces import HivePieces


param_list = [('a', 'a'), ('a', 'b'), ('b', 'b')]

class TestMovmentRules(unittest.TestCase):

    def test_movement_not_possible_if_P1_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P1.piece, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.QueenBee_P2.piece, Coordinate(-1,0)))

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 0)

    def test_movement_not_possible_if_P2_Queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.QueenBee_P1.piece, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P2.piece, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P1.piece, Coordinate(1,0)))        

        #Act
        movementMoves = hiveGame.rules.getMovementMoves()

        #Assert
        self.assertEqual(len(movementMoves), 0)

    @parameterized.expand([ # type: ignore
        ([True,  False, False, False, False, False], False),
        ([True,  False, True,  False, False, False], True),
        ([True,  False, True,  False, False, True ], True),
        ([True,  False, True,  False, True,  False], False),
        ([False, True,  False, True,  False, True ], False),
        ([True,  False, True,  False, False, True ], True),
        ([False, False, True,  True,  False, False], False),
        ([True,  False, False, False, False, True ], False),
        ([False, True,  False, True,  False, False], True),
    ])

    def test_detectBridgingCombinations(self, neighbourPiecesPresent: List[bool], gapExpected: bool):
        #Arrange
        navigationCircle = [
            Direction.LEFT,
            Direction.UP_LEFT,
            Direction.UP_RIGHT,
            Direction.RIGHT,
            Direction.DOWN_RIGHT,
            Direction.DOWN_LEFT
        ]

        board = HiveBoard()
        centerPiece = HivePieces.CreatePieceWithCoordinate(Piece(True, Creatures.Grasshopper,0), Coordinate(1,1))
        board.movePiece(centerPiece)

        for directionIndex in range(0,6):
            if(neighbourPiecesPresent[directionIndex]):
                neighbourCoordinate = board.navigate(navigationCircle[directionIndex], centerPiece.coordinate)
                board.movePiece(HivePieces.CreatePieceWithCoordinate(Piece(True, Creatures.Grasshopper,directionIndex), neighbourCoordinate))

        movementRules = HiveRulesMove(board)

        #Act
        pieces: Optional[Tuple[BoardPiece, BoardPiece]] = movementRules.getBridgingPieces(centerPiece)

        #Assert
        if(gapExpected):
            self.assertIsNotNone(pieces)
        else:
            self.assertIsNone(pieces)            

    def test_no_movement_when_queen_is_not_placed(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Beetle_0_P1.piece, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Beetle_0_P2.piece, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P1.piece, Coordinate(0,1)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P2.piece, Coordinate(-2,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_1_P1.piece, Coordinate(1,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_1_P2.piece, Coordinate(-3,0)))

        print(hiveGame.board.printBoard())

        #Act
        moveablePieces = hiveGame.rules.moveablePieces()

        #Assert
        self.assertEqual(len(moveablePieces), 0)

    def test_movement_possibple_for_all_moveable_pieces(self):
        #Arrange
        hiveGame = HiveGame()
        pieces = hiveGame.board.pieces
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.QueenBee_P1.piece, Coordinate(0,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.QueenBee_P2.piece, Coordinate(-1,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P1.piece, Coordinate(0,1)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_0_P2.piece, Coordinate(-2,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_1_P1.piece, Coordinate(1,0)))
        hiveGame.playMove(HivePieces.CreatePieceWithCoordinate(pieces.Ant_1_P2.piece, Coordinate(-3,0)))

        print(hiveGame.board.printBoard())

        #Act
        moveablePieces = hiveGame.rules.moveablePieces()

        #Assert
        self.assertEqual(len(moveablePieces), 2)

if __name__ == "__main__":
    unittest.main()
