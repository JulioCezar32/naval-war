class GameBoard():

    def __init__(self, size):
        self.size = size
        self.bord = self.set_up_board()

        # Is necessary put the name of bord inside the method name? like create_board_range
    def create_range(self):
        rows_numbers = range(1, self.size + 1)
        columns_letters = "ABCDEFGHIJKLMNOPQRSTUVXZ"[:self.size]
        return (rows_numbers, columns_letters)

    def set_up_board(self):
        rows, columns = self.create_range()
        board = [{column:0 for column in columns} for row in rows]
        return board
