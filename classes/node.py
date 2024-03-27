from collections import deque

class Node:
    connections = []
    def __init__(self, ein):
        self.ein = ein
        self.connections

    def EIN(self):
        return self.ein
    
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
    
    def routes_to(self, target):
        paths = []
        queue = deque([[self]])

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == target:
                if path not in paths:
                    paths.append(path)
                
            for connection in node.connections:
                if connection not in path:
                    queue.append(path + [connection])

        return paths


        