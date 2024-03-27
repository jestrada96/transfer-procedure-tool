from classes.valve import Valve

class Valve3(Valve):
    def __init__(self, ein):
        self.ein = ein

    def report(self):
        print("Valve: ", self.ein)
        pass