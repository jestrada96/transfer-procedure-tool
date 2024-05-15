from utils.node import Node

class Pump(Node):
    directions = 100
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.directions = 100 
        self.node_1 = None
        self.connections = []
        self.show = True
        self.dvi_credited = False
        self.dvi_used   = False
        self.in_tank = True
        