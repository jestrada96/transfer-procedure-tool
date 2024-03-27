from collections import deque

class Node:
    connections = []
    def __init__(self, ein):
        self.ein = ein
        self.connections

    def EIN(self):
        return self.ein
    
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


        