class GameBoard():


    def __init__(self, size):
        self.size = size
        self.range = self.create_range()

        # Is necessary put the name of bord inside the method name? like create_board_range
    def create_range(self):
        return (range(1, self.size + 1),"ABCDEFGHIJKLMNOPQRSTUVXZ"[:self.size ])

    def set_up_board(self):
        rows, columns = self.range
        self.board = [{column:0 for column in columns} for row in rows]
        return self.board
