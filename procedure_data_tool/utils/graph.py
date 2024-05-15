import networkx as nx
import matplotlib.pyplot as plt

def makeGraph(components):
    G = nx.DiGraph()

    for c in components:
        if c:
            G.add_node(c.ein)
            for connection in c.connections:
                 G.add_edge(c.ein, connection.ein)
    
    # for key, value in components.items():
    #     if key:
    #         G.add_node(key)
    #         for connection in value.connections:
    #             G.add_edge(key, connection.ein)

    pos = nx.spring_layout(G)  # Position nodes using the Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_size=80, node_color='skyblue', font_size=9, font_color='black', edge_color='gray', linewidths=2)

    plt.show()