from game_board import *


class PutShip(Game_board):


    def __init__(self, board_size):
        Game_board.__init__(self, board_size)
        self.game_board = Game_board(10)
        rows, seats = self.game_board.create_board()
        self.ship = [None] + [{letter:None for letter in seats} for _ in rows]
        print(rows)
        print(seats)
        print(self.ship)

x = Game_board(10)
b = PutShip(x)
