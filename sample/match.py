from gameboard import GameBoard
class Match(GameBoard):

    def __init__(self, ship_owner, bomb_owner, board_size):
        #receive all data from the match
        self.board = GameBoard(board_size).set_up_board()
        self.ship_owner = ship_owner
        self.bomb_owner = bomb_owner

        self.ship_positions = ship_owner.board_positions
        self.bombs_positions = bomb_owner.bomb_position
        self.plot_ship()

    def plot_ship(self):
        #plot ship into the board
        for ship_position in self.ship_positions:
            for position in ship_position:
                ship_row = position[0]
                ship_column = position[1]
                row = int(ship_row)
            #chance de value of position to 1
            #try:
                self.board[row -1][ship_column] = 1
            #except IndexError:
                #return " Position is not avaible"
                #exit(1)
    def get_result(self):
        for bomb in self.bombs_positions:
            bomb_column = bomb[-1]
            bomb_row = int(bomb[:-1])
            if(self.board[bomb_row - 1][bomb_column] == 1):
                self.board[bomb_row - 1][bomb_column] = 2
        #        print('The ship was hitted bomb :{}'.format(bomb))

            elif(self.board[bomb_row - 1][bomb_column] == 2):
                pass
                #
                print ('The positions alredy bombeb')
            else:
                print ('The ship was not hitted')

    def destroyed_ship(self):
        #plot ship into the board
        for ship_position in self.ship_positions:
            ship_state = []
            list = [0 , 1]
            for position in ship_position:
                ship_row = position[0]
                ship_column = position[1]
                row = int(ship_row)
            #chance de value of position to 1
            #try:
                state_of_ship = self.board[row -1][ship_column]
                ship_state.append(state_of_ship)

            if any(state_of in ship_state for state_of in list):
                print ("ship survived")
            else:
                print ("ship {} defeated".format(ship.name))
            #except IndexError:
                #return " Position is not avaible"
                #exit(1)
