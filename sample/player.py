from ship import Ship


class Player():


    def __init__(self,name):
        self.name = name

    def create_ship(self, Ship, position):
        self.ship = Ship
        self.ship_position = position

    def launch_bomb(self, position):
        self.bomb_position = position
