import time
import sys
import os
from player import HumanPlayer, RandomComputerPlayer


running = True


class TicTacToe:
    """
    Class for the main game and the game board.
    """
    def __init__(self):
        # a list for representing the empty 3x3 board
        self.board = [' ' for _ in range(9)]
        # set the value to the letter of the winner later in the game
        self.current_winner = None

    def print_game_board(self):
        """
        Method for printing the base 3x3 game board.
        Prints a separator between each spot on the board.
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + ' | '.join(row) + ' |')

    @staticmethod
    # a method that is not tied to any classes
    def print_ref_board():
        """
        Method for printing the reference board at the start of the game
        with the indices referring to the correct user input.
        """
        ref_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in ref_board:
            print("| " + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        Method for returning a tuple of the available moves.
        This method is used to validate the get_move method of
        the player class.
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """
        This method returns a boolean value
        based on the instances of whitespaces
        on the board. The play function loops while
        the returned value from this method is True.
        """
        return ' ' in self.board

    # def num_empty_squares(self):
    #     return self.board.count(' ')

    def make_move(self, square, letter):
        """
        Method for assigning each player's letter to the
        board based on their move. Also returns the
        winner if there is one.
        """
        if self.board[square] == ' ':
            # if the intended move is available
            self.board[square] = letter
            # assign player's letter to the spot
            if self.winner(square, letter):
                # assign winner's letter if there is one.
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        """
        Method for checking for a winner, based on the rules
        of tic-tac-toe. The function checks for each row,
        column, and 2 possible diagonal outcomes that.
        """
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def quit(user_input):
    """
    The program quits if the user types in "q" as user input
    """
    if user_input == "q" or user_input == "Q":
        type("thanks for playing")
        return True
    else:
        return False


def type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def play_again():
    pass


def play(game, human, computer, print_game=True):
    """
    This is the main game function that prints the reference
    board, and then the main board. The function loops until
    there are no empy spaces left, or until there is a winner.
    The function also switches between the players after each
    move.
    """
    if print_game:
        # prints out the reference board if print_game is set to True
        game.print_ref_board()

    letter = 'X'
    # X means the first one to make a move is the player
    while game.empty_squares():
        if letter == 'O':
            # if the current value of the letter is O, the computer moves
            # otherwise the player is asked to make a move
            # switching between players happens at the end of the loop,
            # while there is no winner yet, or there are empty spaces left
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            # proceeds if the intended move is valid
            if print_game:
                # print the current player's move
                print(letter + f' makes a move to square {square}')
                # print the updated board
                game.print_game_board()
                # print an empty line after the board
                print('')

            # if game.current_winner:
            #     # triggers if a value was assigned by winner()
            #     # returns the letter of the winner
            #     # ends the game loop
            #     if print_game:
            #         print(letter + ' wins!')
            #     return letter
            #     # print_game = False
            #     # play_again()

            if game.current_winner:
                print(f"{letter} wins!")
                while True:
                    answer = str(input('Run again? (y/n): '))
                    if answer == 'y':
                        type("resetting board...")
                        break
                    elif answer == 'n':
                        print("Goodbye")
                        break
                break

            if letter == 'X':
                # keeps switching players, until winner is assigned
                # or if there is available space left
                letter = 'O'
            else:
                letter = 'X'

            if not game.empty_squares():
                print("It's a tie!")
                while True:
                    ask_player()

       
        # time.sleep(1)
        # a short delay between switching players

    # if print_game:
    #     # if the while loop ends without a winner assigned,
    #     # and there is no empty space left
    #     # print "It's a tie!"
    #     print("It's a tie!")
        



def menu():
    """
    This function is called first, when the program starts running.
    Prints out game title and asks for user input to either 
    proceed to playing or quit the game
    """
    ascii = ("""
 ______   __     ______        ______   ______     ______        ______   ______     ______    
/\__  _\ /\ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\      /\__  _\ /\  __ \   /\  ___\   
\/_/\ \/ \ \ \  \ \ \____     \/_/\ \/ \ \  __ \  \ \ \____     \/_/\ \/ \ \ \/\ \  \ \  __\   
   \ \_\  \ \_\  \ \_____\       \ \_\  \ \_\ \_\  \ \_____\       \ \_\  \ \_____\  \ \_____\ 
    \/_/   \/_/   \/_____/        \/_/   \/_/\/_/   \/_____/        \/_/   \/_____/   \/_____/
    """)
    print('')
    print(ascii)
    print("Welcome to tic-tac-toe")
    print('')
    name = input("Please enter your name: ")
    print('')
    print(f"Welcome {name}!\n\nEnter 's' to start the game or 'q' to quit!")
    user_input = input().lower()
    if user_input == "s":
        type("Game is starting...")
        time.sleep(1)
        os.system("cls")
        os.system("clear")
        play(t, x_player, o_player, print_game=True)
       


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    menu()
