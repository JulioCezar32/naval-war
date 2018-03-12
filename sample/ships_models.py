from ship import Ship

class Encouracado(Ship):


    def __init__(self, position):

        ship_size = 3
        Ship.__init__(self,'Encouracado', position, ship_size)


class PortaAvioes(Ship):


    def __init__(self, position):

        ship_size = 3
        Ship.__init__(self,'PortaAvioes', position, ship_size)
