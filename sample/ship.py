from player import Player
class Ship():

    def __init__(self, Player):
        self.position = Player.ship_position

    def get_position(self):
        return self.position
