from classes.valve import Valve

class Valve2(Valve):
    directions = 2
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.directions = 2 
        self.node_1 = None
        self.node_2 = None
        self.connections = []
        self.show = True
        self.in_tank = False
