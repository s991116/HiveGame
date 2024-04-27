from HiveGame import HiveGame

game = HiveGame()

while(True):
  #Get Moves
  moves = game.getValidMoves()

  #Print Moves
  print("Valid Moves")
  moveIndex = 0
  for move in moves:
    print(str(moveIndex) + ":" + move.print())
    moveIndex += 1

  #Select Move
  moveIndex = input("Select move index (-1 to quit):")

  if(int(moveIndex) < 0):
    break

  game.playMove(moves[int(moveIndex)])

  #Print Board
  print(game.board.printBoard())
