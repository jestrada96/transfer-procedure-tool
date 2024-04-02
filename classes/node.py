from collections import deque

class Node:
    connections = []
    def __init__(self, ein):
        self.ein = ein
        self.connections

    def EIN(self):
        return self.ein
    
    def __str__(self):
        return self.ein
    
    def connectBack(self, node):
        if node in self.connections: return
        elif len(self.connections) < self.ways: self.connect(node)
        else: print(self.EIN(), "has maximum number of connections")
        return

    def connect(self, *nodes):
        for node in nodes[:self.ways]:
            if node:
                if len(self.connections) < self.ways:
                    self.connections.append(node)
                    node.connectBack(self)
                else:  
                    print("has maximum number of connections")
        # Not working now that there is no "None" as connection.

    def report(self):
        print((self.EIN()), "connections: ")
        for node in self.connections:
            if (node):
                print(node.EIN())
            else:
                print("Missing Connection")
    
    def routesTo(self, target, num_routes = 1):
        paths = []
        queue = deque([[self]])

        while queue and len(paths) < num_routes:
            path = queue.popleft()
            node = path[-1]

            if node == target:
                if path not in paths:
                    paths.append(path)
                
            for connection in node.connections:
                if connection not in path:
                    queue.append(path + [connection])

        return paths


        