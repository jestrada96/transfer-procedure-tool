from classes.node import Node

class Valve(Node):
    connections = []
    ways = 10
    def __init__(self, ein):
        self.ein = ein
        self.connections
        self.ways

    def connect_back(self, node):
        if node in self.connections: return
        elif len(self.connections) < self.ways: self.connect(node)
        else: print(self.EIN(), "has maximum number of connections")
        return

    def connect(self, *nodes):
        for node in nodes[:self.ways]:
            if node:
                if len(self.connections) < self.ways:
                    self.connections.append(node)
                    node.connect_back(self)
                else: 
                    print("has maximum number of connections")

    def report(self):
        print((self.EIN()), "connections: ")
        for node in self.connections:
            if (node):
                print(node.EIN())
            else:
                print("Missing Connection")
# Not working now that there is no None as connection.
                
        