class Ship():

    def __init__(self, name, ship_head, ship_size):
        self.ship_head = ship_head
        self.name = name
        self.size = ship_size
        self.generate_position()
        #pensar numa nova nomenclatura
    def generate_position(self):
        self.position = []
        ship_column = self.ship_head[1]
        ship_row = self.ship_head[0]
        for pera in range(self.size):
            ship_next_row = int(self.ship_head[0]) + pera
            ship_body = str(ship_next_row) + ship_column
            self.position.append(ship_body)
