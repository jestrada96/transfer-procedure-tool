from classes.valve import Valve
class Valve2(Valve):
    def __init__(self, ein):
        self.ein = ein

    def report(self):
        print("Valve: ", self.ein)
        pass