class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print-board(self):
        for rown in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + ' | '.join(row) + ' |')