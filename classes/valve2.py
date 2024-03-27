from classes.valve import Valve

class Valve2(Valve):
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.ways = 2 
        self.node_1 = None
        self.node_2 = None
        self.connections = []
