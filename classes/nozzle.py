from classes.node import Node

class Nozzle(Node):
    directions = 3
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.directions = 3
        self.node_1 = None
        self.node_2 = None
        self.connections = []
        self.show = False
        self.in_tank = False

    def EIN(self):
        return None