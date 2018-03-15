from ship import Ship
from gameboard import GameBoard
class Match(GameBoard):

    def __init__(self, ship_owner, bomb_owner, board_size):
        #receive all data from the match
        self.board = GameBoard(board_size).set_up_board()
        self.ship_owner = ship_owner
        self.bomb_owner = bomb_owner

        self.ship_positions = ship_owner.ship.get_position()
        self.bomb_position = bomb_owner.bomb_position

    def plot_ship(self):
        #plot ship into the board
        for ship_position in self.ship_positions:
            ship_row = ship_position[0]
            ship_column = ship_position[1]
            row = int(ship_row)
            #chance de value of position to 1
            #try:
            self.board[row -1][ship_column] = 1
            #except IndexError:
                #return " Position is not avaible"
                #exit(1)
    def get_result(self):

        bomb_column = self.bomb_position[-1]
        bomb_row = int(self.bomb_position[:-1])
        if(self.board[bomb_row - 1][bomb_column] == 1):
            return 'The ship was hitted'
        else:
            return 'The ship was not hitted'
    def get_board(self):
        return self.board
