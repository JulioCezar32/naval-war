class Player():

    def __init__(self, name):
        self.name = name
        self.ships = []
        self.board_positions = []
        self.board_position_validation = []
        self.bomb_position = []

    def create_ship(self, ship):
        self.ships.append(ship)
        self.camaleao = self.verify_if_ship_will_be_choked(ship)
        self.board_positions.append(ship.position)
        #print(self.camaleao)

    def launch_bomb(self, position):
        self.bomb_position.append(position)

    def verify_if_ship_will_be_choked(self, ship):
        if any(x in self.board_position_validation for x in ship.position):
            return "The Ship {} was inserted into a wrong position".format(ship.name)
        else:
            self.board_position_validation.extend(ship.position)
            return "Ship {} inserted correctly".format(ship.name)
