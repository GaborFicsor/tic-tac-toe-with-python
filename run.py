"""
time and sys for delaying the print functions
os for clearing the terminal
random for making computer's choice
"""
import time
import sys
import os
import random


# the Player superclass, its subclasses and methods
# and the TicTacToe class and play function was made
# with the help of
# https://www.youtube.com/watch?v=8ext9G7xspg&t=2154s
# tutorial
# this can also be found in the credits section of README.md
class Player:
    """
    Class for players represented by the letters
    that are used in tic-tac-toe.
    """
    def __init__(self, letter):
        # the letter will be either X(HumanPlayer), or O(RandomComputerPlayer)
        self.letter = letter


class RandomComputerPlayer(Player):
    """
    Subclass of the Player parent class that defines the computer player
    and the method used for making their move.
    """

    def get_move(self, game):
        """
        Method for generating the computer's random move
        based on the available spots on the board.
        """
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    """
    Subclass of the Player parent class that defines the Human player
    and the method used for making their move.
    """

    def get_move(self, game):
        """
        Method for asking and validating the player's move based on
        available spots left on the game board, and checking
        for valid input.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input("Make your move(1-9):\n")
            print('')
            if square.isalpha():
                print("Please enter whole numbers only.\n")
            elif not square or square.isspace():
                print("Whitespaces or blank input can not be entered.\n")
            elif not square.isdigit():
                print("Input can not contain floats, strings or negative\
 numbers.\n")
            else:
                try:
                    val = int(square) - 1
                    if val < 0 or val >= 9:
                        raise IndexError
                    elif val not in game.available_moves():
                        valid_square = True
                        raise ValueError
                    valid_square = True
                except ValueError:
                    print("That spot is already taken. Please try again.\n")
                except IndexError:
                    print("Number must be between 1 and 9.\n")

        return val


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
        Also prints a separator between each spot on the board.
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
        ref_board = [[str(i+1) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in ref_board:
            print("| " + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        Method for returning a list of the available moves.
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
            # checking for rows that contain the same letter 3 times.
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            # checking for columns that contain the same letter 3 times.
            return True

        if square % 2 == 0:
            # checking if the 2 diagonals that contain the same letter 3 times.
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False


def type_slow(text):
    """
    Function to make game type text instead of printing.
    Makes the game a little more satisfying to read.
    """
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.05)


def go_first():
    """
    Function to let the player decide, whether he wants to
    go first, or make the computer go first.
    """
    letter = None
    while True:
        start = input("Would you like to start ('Y'),\
 or let the computer go first('N')? Y/N:\n").lower()
        if start == "y":
            letter = "X"
            return letter
        elif start == "n":
            letter = "O"
            return letter
        else:
            print("\nPlease enter 'Y' if you want to go first,\
 or 'N' to let the computer go first.\n")


def play(game, x_player, o_player, name, print_game=True):
    """
    The function for the game to loop until there is a
    winner, or there are no blank spots left.
    """
    if print_game:
        letter = go_first()
    print("\nReference board:\n")
    game.print_ref_board()
    print("\nThe numbers on the board represent the input you need to type.\n")
    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                if letter == "X":
                    type_slow(f"{name} makes a move to square {square + 1}")
                else:
                    type_slow(f"Computer makes a move to square {square + 1}")
                print('')
                game.print_game_board()
                print('')

            if game.current_winner:
                if print_game:
                    if letter == "X":
                        print(f"\n{name} wins!")
                    else:
                        print("\nComputer wins!")
                return letter

            letter = "O" if letter == "X" else "X"
            # alternate between letters for each player's turn
        time.sleep(1)

    if print_game:
        # if there is no blank spot left, the game ends with a tie
        print("\nIt's a tie!")
        return None


def wipe():
    """
    Function to declutter terminal
    """
    os.system("cls")
    os.system("clear")


def get_name():
    """
    Function to ask for the user's name and store it
    """
    while True:
        name = input("Please enter your name:\n")
        if not name or name.isspace():
            print("\nName can not be blank.\n")
        elif name.lower() == "blank":
            print("\nNice try!\n")
        elif name.lower() == "computer" or name.lower() == "comp":
            print("\nName can not be Computer.\n")
        else:
            return name


def instructions():
    """
    Function to store user's name and give short instructions on
    how to play the game
    """
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tic_tac_toe = TicTacToe()
    name = get_name()
    type_slow(f"\nWelcome {name}!\n")
    time.sleep(0.2)
    type_slow("\nYour letter is 'X'.\n")
    time.sleep(0.2)
    type_slow("\nThe Computer's letter is 'O'.\n")
    time.sleep(0.2)
    type_slow("\nFirst one to line up three of their letters wins!\n")
    time.sleep(0.2)
    print("\nPlease enter 'S' to start the game or 'Q' to quit.")
    while True:
        decision = input().lower()
        if decision == "s":
            type_slow("\nSetting up board...")
            time.sleep(0.5)
            wipe()
            play(tic_tac_toe, x_player, o_player, name, print_game=True)
            return
        elif decision == "q":
            type_slow("\nThanks for playing!")
            time.sleep(1)
            wipe()
            exit()
        else:
            print("Please enter 'S' to start or 'Q' to quit")


def main():
    """
    This function is called first, when the program starts running.
    Prints out game title and asks for user input to either
    proceed to playing or quit the game
    """
    ascii_title = (r"""
    __  .__                   __                            __
  _/  |_|__| ____           _/  |______    ____           _/  |_  ____   ____
  \   __\  |/ ___\   ______ \   __\__  \ _/ ___\   ______ \   __\/  _ \_/ __ \
   |  | |  \  \___  /_____/  |  |  / __ \\  \___  /_____/  |  | (  <_> )  ___/
   |__| |__|\___  >          |__| (____  /\___  >          |__|  \____/ \___  >
                \/                     \/     \/                            \/
""")
    print('')
    print(ascii_title)
    print("Welcome to tic-tac-toe!".center(80))
    print('')
    print("press enter to start the game".center(80))
    user_input = input().lower()
    if user_input == "":
        type_slow("Game is starting...")
        time.sleep(1)
        wipe()
        instructions()
        while True:
            print("\nWould you like to play again? Y/N:\n")
            user_input = input().lower()
            if user_input == "y":
                wipe()
                instructions()
            elif user_input == "n":
                type_slow("\nThanks for playing!")
                time.sleep(1)
                wipe()
                break
            else:
                print("\nPlease enter either 'Y' or 'N'")


if __name__ == '__main__':
    main()
