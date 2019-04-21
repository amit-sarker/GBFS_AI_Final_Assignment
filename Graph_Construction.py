import random

import networkx as nx


def construct_graph(nodes, edges):
    G = nx.gnm_random_graph(nodes, edges)
    directed_graph = nx.DiGraph()
    directed_graph.add_nodes_from(G)
    directed_graph.add_edges_from(G.edges)

    for (u, v, w) in directed_graph.edges(data=True):
        directed_graph.edges[u, v]['weight'] = random.randint(1, 10)

    print("Constructed Graph:")
    print(directed_graph.edges(data=True))
    print('\n')

    return directed_graph


