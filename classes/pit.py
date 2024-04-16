from classes.node import Node

class Pit():
    def __init__(self, name, nace = None, nacePMID = None):
        self.name = name
        self.nace = nace
        self.nacePMID = nacePMID
        self.heaters = []
        self.tfsps = []
        self.tfsps_pmid = []
        self.nodes = []