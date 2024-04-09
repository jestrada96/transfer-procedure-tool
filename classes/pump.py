from classes.node import Node

class Pump(Node):
    directions = 1
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.directions = 1 
        self.node_1 = None
        self.connections = []
        self.show = True
        self.dvi_credited = False
        self.dvi_used   = False