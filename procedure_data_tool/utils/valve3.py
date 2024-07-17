from procedure_data_tool.utils.valve import Valve

class Valve3(Valve):
    directions = 3
    blocked_element = None
    def __init__(self, ein, pit = None, jumper = None, jumperLabel = None, dvi = None):
        super().__init__(ein, pit= pit, jumper = jumper)
        self.directions = 3
        self.ein = ein
        self.connections = []
        self.show = True
        self.in_tank = False
        self.position
        self.dvi_credited = dvi
        self.blocked_element

    def setPosition(self, route = None):
        for connection in self.connections:
            if connection in route:
                pass
            else:
                self.blocked_element = connection
                if connection.EIN():
                    self.position = "BLOCK " +  self.blocked_element.EIN()
                else:
                    for next_connection in self.blocked_element.connections:
                        if next_connection == self or next_connection in self.connections:
                            pass
                        else:
                            self.position = "BLOCK " + next_connection.EIN()

    def findDVI(self, route):
        self.dvi_used = self.dvi_credited #CORRECT. ALWAYS
        for connection in self.connections:
            if connection in route:
                pass
            else:
                if connection.EIN():
                    route.append(connection)
                else:
                    for next_connection in connection.connections:
                        if next_connection == self or next_connection in self.connections:
                            pass
                        else:
                            route.append(next_connection)
        return 
    
    def getColor(self):
        if (self.dvi_used == "YES"):
            self.color = "steelblue"
        elif (self.dvi_used == "POS"):
            self.color = "indianred"
        if (self.dvi_used == "NO"):
            self.color = "lightgray"
        return self.color