from procedure_data_tool.utils.node import Node

class Valve(Node):
    connections = []
    directions = 0
    def __init__(self, ein, jumper = None, jumperLabel = None):
        self.ein = ein
        self.connections
        self.directions
        self.show = True
        self.in_tank = False
        self.jumper = jumper
        self.jumperLabel = jumperLabel
                
        