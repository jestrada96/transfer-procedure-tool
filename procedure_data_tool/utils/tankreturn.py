from procedure_data_tool.utils.node import Node

class TankReturn(Node):
    directions = 1
    def __init__(self, ein):
        super().__init__(ein) 
        self.ein = ein
        self.directions = 1 
        self.node_1 = None
        self.connections = []
        self.show = True
        self.dvi_credited = False
        self.dvi_used  = False
        self.in_tank = True

        # HAVE EIN OUTPUT JUST THE LABEL (Last character)
        def EIN(self):
            return None
