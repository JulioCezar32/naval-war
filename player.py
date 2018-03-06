class Player():


    def __init__(self,name):
        self.name = name

    def create_ship(self, ship, posicao):
        self.ship = ship
        self.ship_posicao = posicao

    def launch_bomb(self, posicao):
        self.bomb_posicao = posicao

    
