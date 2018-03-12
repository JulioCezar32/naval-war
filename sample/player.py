class Player():


    def __init__(self, name):
        self.name = name

    def create_ship(self, choosed_ship):
        self.ship = choosed_ship

    def launch_bomb(self, position):
        self.bomb_position = position
