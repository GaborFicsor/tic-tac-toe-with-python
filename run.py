import time
from player import HumanPlayer, RandomComputerPlayer


class TicTacToe:
    """
    Class for the main game and the game board.
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        """
        Method for printing the base 3x3 game board.
        Prints a separator between each spot on the board.
        """
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        """
        Method for printing the reference board with the indices
        referring to the correct user input.
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
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
            self.board[square] = letter
            if self.winner(square, letter):
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


def play(game, human, computer, print_game=True):
    """
    This is the main game function that prints the reference
    board, and then the main board. The function loops until
    there are no empy spaces left, or until there is a winner.
    The function also switches between the players after each
    move.
    """
    if print_game:
        game.print_board_nums()

    letter = 'X'
    while game.empty_squares():
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'

        time.sleep(1)

    if print_game:
        print("It's a tie!")


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
