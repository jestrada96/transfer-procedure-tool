from classes.node import Node

class Split(Node):
    directions = 3
    def __init__(self, ein, node_1 = None, node_2 = None, node_3 = None):
        super().__init__(ein)
        self.directions = 3; 
        self.ein = ein
        self.node_1 = node_1
        self.node_2 = node_2
        self.node_3 = node_3
        self.connections = []
        self.show = False
        self.in_tank = False
        self.onJumper = False
        
    def EIN(self):
        return None
