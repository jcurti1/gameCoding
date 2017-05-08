# Creating a Tic Tac Toe Game

#global constants
X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARE = 9


#Instructions function for Tic Tac Toe Game
def instructions():
    """Displaying the games instructions"""
    print("Welcome to Tic Tac Toe!!\n"
          "The Instructions to how you play the game are shown below.\n"
          "This game will be between the computer and your human brain\n"
          "You will make your move by entering a number between 0 - 8\n"
          "The number will represent the postion on the board as illustrated below:\n"
          "0 | 1 | 2\n"
          "---------\n"
          "3 | 4 | 5\n"
          "---------\n"
          "6 | 7 | 8\n\n"
          "Test yourself as the game is about to begin.\n")

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in("y", "n"):
        response = raw_input(question)
        return response

def ask_number(question,low, high):
    """Ask for a number within range"""
    response = None
    while response not in range(low,high):
        response = int(input(question))
    return response

def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARE):
        board.append(EMPTY)
    return board


#main start code
instructions()
