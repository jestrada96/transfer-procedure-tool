import networkx as nx
import matplotlib.pyplot as plt

def makeGraph(inventory, route, simple_route, layout_type='Kamada Kawai'):
    G = nx.Graph()

    color_map = []
    size_map = []
    for component in route:
        if component:
            G.add_node(component.ein)
            for connection in component.connections:
                 G.add_edge(component.ein, connection.ein)
    
    for i in range(len(simple_route) - 1):
        if G.has_edge(simple_route[i].ein, simple_route[i + 1].ein):
            G.edges[simple_route[i].ein, simple_route[i + 1].ein]['color'] = 'red'

    # Set default edge color for all other edges
    default_edge_color = 'gray'
    for u, v in G.edges:
        if 'color' not in G[u][v]:
            G.edges[u,v]['color'] = default_edge_color

    for node in G:
        color_map.append(inventory[node].getColor())
        size_map.append(inventory[node].size)


    edge_colors = [G[u][v]['color'] for u, v in G.edges]

    size_map[0] = 300
    size_map[-1] = 300
    layout_functions = {
        "Pyramid": nx.planar_layout,
        "Arch" : nx.spectral_layout,
        "Zig-zag": nx.kamada_kawai_layout
    }

    color_legend = {
        "Transfer Line" : "white",
        "Tank Return / Dropleg" : "lightgreen",
        "Pump" : "mediumpurple",
        "Pit Nozzle" : "gray",
        "DVI Valve" : "steelblue",
        "Position-Dependent DVI Valve" : "indianred",
        "Non-DVI Valve" : "lightgray",
    }
    try:
        pos = layout_functions[layout_type.get()](G)
    except KeyError:
        raise ValueError("Invalid layout type specified")
    
    fig = plt.figure()
    plt.title = "Route Preview"
    nx.draw(G, pos, with_labels=True, edge_color=edge_colors, node_size= size_map, node_color=color_map, font_size=9, font_color='black', linewidths=10)

    legend_handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor=color, markersize=10) for color in color_legend.values()]
    legend_labels = [key for key in color_legend.keys()]

    plt.legend(legend_handles, legend_labels, loc='best', title='Legend', fontsize='medium')
    plt.show()