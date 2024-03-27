from classes.valve import Valve

class Valve3(Valve):
    def __init__(self, ein, node_1 = None, node_2 = None, node_3 = None):
        super().__init__(ein)
        self.ways = 10; #fix
        self.ein = ein
        self.node_1 = node_1
        self.node_2 = node_2
        self.node_3 = node_3
        self.connections = []

