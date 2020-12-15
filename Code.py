#--------- Global Variables -----------

# Board to hold our game
BOARD = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Lets us know if the game is over yet
GAME_STILL_GOING = True

# Tells us who the WINNER is
WINNER = None

# Tells us who the current player is (X goes first)
CURRENT_PLAYER = "X"


# ------------ Functions --------------

# Play a game of tic tac toe (overarching game logic)
'''
Input: nothing
Output: nothing
What it does: calls all the other functions to make the
entire game run
'''
def play_game():
  
  # Shows initial BOARD 
  display_board()

  # game loop
  while GAME_STILL_GOING:

    handle_turn(CURRENT_PLAYER)

    check_if_game_over()

    flip_player()

  # Check if the WINNER global variable is "X" or "O", meaning somebody
  # won, and if so, print out the winner.
  # else print that there was a tie
  if WINNER == 'X':
    print("The Play X won!")
  elif WINNER == 'O':
    print("The play O won!")
  elif WINNER == None:
    print("It is a tie!")
  
  #return WINNER



# Display the game BOARD to the screen (print the BOARD)
'''
Input: nothing
Output: nothing
What it does: reads the game BOARD list and prints it 
to the screen
'''
def display_board():
  print()
  print(BOARD[0:3])
  print(BOARD[3:6])
  print(BOARD[6:9])
  positions = [1,2,3,4,5,6,7,8,9]
  print(positions[0:3])
  print(positions[3:6])
  print(positions[6:9])
  return 


 
# Handle a turn for an arbitrary player
'''
Input: The current player as a string ("X" or "O")
Output: nothing
What it does: takes one player, and handles their entire turn
'''
def handle_turn(player):

  # Get the position from player
  print(player + "'s turn.")
  position = input("Choose a position from 1-9: ")

  # Whatever the user inputs, make sure it is a valid input, and the spot is open
  valid = False
  while not valid:

    # Make sure the input is valid
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Choose a position from 1-9: ")

    # Get correct index in our board list
    position = int(position) - 1

    # Then also make sure the spot is available on the board
    if BOARD[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # take the positio variable (it's a string)
  # then input player variable into the board variable
  BOARD[position] = player
  display_board()



# Check to see if the game should be over
'''
Input: nothing
Output: nothing
What it does: checks if there's a game over
'''
def check_if_game_over():
  check_for_winner()
  check_for_tie()



# Check if there is a tie on the BOARD
'''
Input: nothing
Output: True or False
What is does: Checks if there is a tie
'''
def check_for_tie():
  # figure out the conditions for a tie
  global GAME_STILL_GOING
  if '-' not in BOARD:
    GAME_STILL_GOING = False



# Check to see if somebody has won
'''
Input: nothing
Output: nothing
What it does: checks to see if one of the players won
'''
def check_for_winner():

  global WINNER

  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  
  if row_winner:
    WINNER = row_winner
  elif column_winner:
    WINNER = column_winner
  elif diagonal_winner:
    WINNER = diagonal_winner
  else:
    WINNER = None



# Check the rows for a win
'''
Input: nothing
Output: None if there is no win, or "X" or "O" if there was a win
What it does: Checks the rows for a win
'''
def check_rows():

  global GAME_STILL_GOING

  if BOARD[0] == BOARD[1] == BOARD[2] != '-':
    GAME_STILL_GOING = False
    return BOARD[0]
  elif BOARD[3] == BOARD[4] == BOARD[5] != '-':
    GAME_STILL_GOING = False
    return BOARD[3]
  elif BOARD[6] == BOARD[7] == BOARD[8] != '-':
    GAME_STILL_GOING = False
    return BOARD[6]
  else:
    return None



# Check the columns for a win
'''
Input: nothing
Output: None if there is no win, or "X" or "O" if there was a win
What it does: Checks the columns for a win
'''
def check_columns():
  global GAME_STILL_GOING

  if BOARD[0] == BOARD[3] == BOARD[6] != '-':
    GAME_STILL_GOING = False
    return BOARD[0]
  elif BOARD[1] == BOARD[4] == BOARD[7] != '-':
    GAME_STILL_GOING = False
    return BOARD[1]
  elif BOARD[2] == BOARD[5] == BOARD[8] != '-':
    GAME_STILL_GOING = False
    return BOARD[2] 
  else:
    return None



# Check the diagonals for a win
'''
Input: nothing
Output: None if there is no win, or "X" or "O" if there was a win
What it does: Checks the diagonals for a win
'''
def check_diagonals():

  global GAME_STILL_GOING

  if BOARD[0] == BOARD[4] == BOARD[8] != '-':
    GAME_STILL_GOING = False
    return BOARD[0]
  elif BOARD[6] == BOARD[4] == BOARD[2] != '-':
    GAME_STILL_GOING = False
    return BOARD[6]
  else:
    return None



# Flip the current player from X to O, or O to X
'''
Input: nothing
Output: nothing
What it does: flips the player
'''
def flip_player():
  # Global variables we need access to
  global CURRENT_PLAYER

  if CURRENT_PLAYER == 'X':
    CURRENT_PLAYER = 'O'
  else:
    CURRENT_PLAYER = 'X'

  # 

  return



# ------------ Start Execution -------------

# Play a game of tic tac toe
play_game()
