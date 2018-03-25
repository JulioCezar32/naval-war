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

        SIZE = 3
        NAME = 'Submarino'
        Ship.__init__(self, NAME, position, SIZE)

class Destroyer(Ship):


    def __init__(self, position):

        SIZE = 3
        NAME = 'Destroyer'
        Ship.__init__(self, NAME,  position, SIZE)

class BarcoDePatrulha(Ship):


    def __init__(self, position):

        SIZE = 2
        NAME = 'BarcoDePatrulha'
        Ship.__init__(self, NAME, position, SIZE)
