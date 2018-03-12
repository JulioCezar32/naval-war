class GameBoard():


    def __init__(self, board_size):
        self.board_size = board_size

    def create_board(self):
        return (range(1, self.board_size ),"ABCDEFGHIJKLMNOPQRSTUVXZ"[:self.board_size + 1])
