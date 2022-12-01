import time
import sys
import os
import random


class Player:
    """
    Class for players represented by the letters
    that are used in tic-tac-toe.
    """
    def __init__(self, letter):
        # the letter will be either X(HumanPlayer), or O(RandomComputerPlayer)
        self.letter = letter

    def get_move(self, game):
        """
        Method for validating each player's intented move.
        """


class RandomComputerPlayer(Player):
    """
    Subclass of the Player parent class that defines the computer player
    and the method used for making their move.
    """
    # def __init__(self, letter):
    #     super().__init__(letter)

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
    # def __init__(self, letter):
    #     super().__init__(letter)

    def get_move(self, game):
        """
        Method for asking and validating the player's move based on
        available spots left on the game board, and checking
        for valid input.
        """
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move(0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid square. Try again.")

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


def type(text):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)


def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_ref_board()
    letter = "X"

    while game.empty_squares():
        if letter == "O":
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, letter):
            if print_game:
                print(f"{letter} makes a move to square {square}")
                game.print_game_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(f"{letter} wins!")
                return letter

            letter = "O" if letter == "X" else "X"

    if print_game:
        print("its a tie!")
        return None


def instructions():
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    name = input("Please enter your name: ")
    print(f"Welcome {name}!")
    print(f"{name}'s symbol is X\nWhile the computer's symbol is O\nYou will make the first move")
    print("Please Enter 's' to start the game or 'q' to quit!")
    while True:
        decision = input().lower()
        if decision == "s":
            os.system("cls")
            os.system("clear")
            play(t, x_player, o_player, print_game=True)
            return
        elif decision == "q":
            print("Thanks for playing!")
            break


def menu():
    """
    This function is called first, when the program starts running.
    Prints out game title and asks for user input to either
    proceed to playing or quit the game
    """
    ascii = (r"""
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
    print("please press enter to start the game")
    user_input = input().lower()
    if user_input == "":
        type("Game is starting...")
        time.sleep(1)
        os.system("cls")
        os.system("clear")
        instructions()
        while True:
            print("Play again? Y/N: ")
            user_input = input().lower()
            if user_input == "y":
                os.system("cls")
                os.system("clear")
                instructions()
            elif user_input == "n":
                print("thanks for playing!")
                os.system("cls")
                os.system("clear")
                break


if __name__ == '__main__':
    while True:
        menu()
