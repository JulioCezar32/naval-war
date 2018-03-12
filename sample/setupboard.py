from gameboard import GameBoard

class SetUpBoard(GameBoard):


    def __init__(self, board_size):
        GameBoard.__init__(self, board_size)
        self.game_board = GameBoard(board_size)
        rows, columns = self.game_board.create_board()
        self.board = [None] + [{letter:None for letter in columns} for _ in rows]

    def get_board(self):
        return self.board