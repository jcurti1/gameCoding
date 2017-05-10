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
        response = input(question)
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

def pieces():
    """Determine if player or computer will go first"""
    go_first = ask_yes_no("do you want to make the first move? (y/n): ")
    if go_first == "y":
        print("\nThen take the first move. You will need it.")
        human = X
        computer = O
    else:
        print("\nThat is your choice but you will regret that!")
        computer = X
        human = O
    return computer, human

def display_board(board):
    """Display game board on screen"""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "---------")
    print("\n\t", board[3], "|", board[4], "|", board[5])
    print("\t", "---------")
    print("\n\t", board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARE):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0,1,2),(3,4,5),(6,7,8),
                   (0,3,6),(1,4,7),(2,5,8),
                   (0,4,8),(2,4,6))
    for row in WAYS_TO_WIN:
        if board[row[0]]==board[row[1]]==board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE

    return None

def human_move(board,human):
    """Get human move."""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Where will you move? (0 - 8):", 0, NUM_SQUARE)
        if move not in legal:
            print("\nThat square is already occupied, PAY ATTENTION! Choose another position to move to.\n")
    print("Fine..")
    return move

def computer_move(board,computer,human):
    """Computer makes a mvove."""
    # make a copy to work with since function will be changing list
    board = board[:]

    #AI code
    #the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number", end=" ")

   # print("I shall take square number")

    #check if computer can win, take it
    for move in legal_moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        #done checking this move, undo it
        board[move] = EMPTY

    #check if human can win, block it
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
    # done checking this mmove, undo it
        board[move] = EMPTY

    #since no one can win, now pick best postion that is left
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """switching turns"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner,computer,human):
    """congratulate winner"""
    if the_winner != TIE:
        print(the_winner, "won!\n")
    else:
        print("It's a tie!\n")

    if the_winner == computer:
        print("As I warned you, human.  You can't defeat a computer!!")
    elif the_winner == human:
        print("I can't believe I lost to you!!  I dare you to play me again!")
    elif the_winner == TIE:
        print("You were most lucky, human, and some how manage to tie me.  This is the best you will ever get.")


#main start code

def main():
    instructions()
    computer,human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board,human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner,computer,human)


#start the program
main()

input("\n\nPress the enter key to quit.")
