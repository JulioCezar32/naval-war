from ship import Ship

class Encouracado(Ship):


    def __init__(self, position):

        SIZE = 4
        NAME = 'Encouracado'
        Ship.__init__(self, NAME, position, SIZE)


class PortaAvioes(Ship):


    def __init__(self, position):

        SIZE = 5
        NAME = 'PortaAvioes'
        Ship.__init__(self, NAME, position, SIZE)

class Submarino(Ship):


    def __init__(self, position):

        ship_size = 3
        Ship.__init__(self,'PortaAvioes', position, ship_size)

class Destroyer(Ship):


    def __init__(self, position):

        ship_size = 3
        Ship.__init__(self,'PortaAvioes', position, ship_size)

class BarcoDePatrulha(Ship):


    def __init__(self, position):

        ship_size = 2
        Ship.__init__(self,'PortaAvioes', position, ship_size)
