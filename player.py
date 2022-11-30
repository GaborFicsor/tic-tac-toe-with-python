import random


class Player:
    """
    Class for players represented by the letters
    that are used in tic-tac-toe.
    """
    def __init__(self, letter):
        # the letter is either X, or O based on the rules of tic-tac-toe
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
        method for validating the computer's move
        based on available spots left on the game board
        and generating it's choice by random.
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
