from ship import Ship

class Encouracado(Ship):

    ship_size = 3

    def __init__(self, position):
        Ship.__init__(self,'Encouracado', position)


class PortaAvioes(Ship):

    ship_size = 3

    def __init__(self, position):
        Ship.__init__(self,'PortaAvioes', position)
