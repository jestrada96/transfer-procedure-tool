import networkx as nx
import matplotlib.pyplot as plt

def makeGraph(inventory, route):
    G = nx.Graph()

    color_map = []
    for component in route:
        if component:
            G.add_node(component.ein)
            for connection in component.connections:
                 G.add_edge(component.ein, connection.ein)
    
    # for key, value in components.items():
    #     if key:
    #         G.add_node(key)
    #         for connection in value.connections:
    #             G.add_edge(key, connection.ein)

    for node in G:
        color_map.append(inventory[node].getColor())
    # pos = nx.planar_layout(G)  
    # pos = nx.spectral_layout(G)
    pos = nx.kamada_kawai_layout(G)
    fig = plt.figure()
    plt.title = "Route Preview"
    nx.draw(G, pos, with_labels=True, node_size=80, node_color=color_map, font_size=9, font_color='black', edge_color='gray', linewidths=10)

    unique_colors = list(set(color_map))
    color_legend = {color: f"Component type {unique_colors.index(color)}" for color in unique_colors}

    # Create legend handles and labels
    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in unique_colors]
    legend_labels = [color_legend[color] for color in unique_colors]

    # Add legend to the plot
    plt.legend(legend_handles, legend_labels, loc='best', title='Legend', fontsize='medium')
    plt.show()