class Ship():

    def __init__(self, name, ship_head, ship_size):
        self.ship_head = ship_head
        self.name = name
        self.size = ship_size

    def get_position(self):
        self.position = []
        for piece in range(self.size):
            next_space = str(int(self.ship_head[0]) + piece) + self.ship_head[1]
            self.position.append(next_space)
        return self.position
