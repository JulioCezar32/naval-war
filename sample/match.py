from ship import Ship


class Match():

    def __init__(self, ship_owner, bomb_owner, board):

        self.ship_owner = ship_owner
        self.bomb_owner = bomb_owner
        self.ship_positions = ship_owner.ship.get_position()
        self.bomb_position = bomb_owner.bomb_position
        self.board = board

        #plot ship into the board
        for ship_position in self.ship_positions:
            ship_column = ship_position[-1]
            ship_row = ship_position[:-1]
            row = int(ship_row)
            self.board[row][ship_column] = 1

    def get_result(self):
        bomb_column = self.bomb_position[-1]
        bomb_row = int(self.bomb_position[:-1])
        if(self.board[bomb_row][bomb_column] == 1):
            return 'The ship was hitted'
        else:
            return 'The ship was not hitted'
