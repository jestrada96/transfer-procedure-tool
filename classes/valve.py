from classes.node import Node

class Valve(Node):
    def __init__(self, ein):
        self.ein = ein

    def report(self):
        print("Valve: ", self.ein)
        pass