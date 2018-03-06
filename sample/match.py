from ship import Ship


class Match():

    def __init__(self, ship_owner, bomb_owner):

        self.ship_owner = ship_owner
        self.bomb_owner = bomb_owner
        self.ship_position = ship_owner.ship_position
        self.bomb_position = bomb_owner.bomb_position

    def get_result(self):
        if(self.ship_position == self.bomb_position):
            return 'The ship was hitted'
        else:
            return 'The ship was not hitted' 
