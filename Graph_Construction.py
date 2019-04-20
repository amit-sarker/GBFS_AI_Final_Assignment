import random

# import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def construct_graph(nodes, edges):
    G = nx.gnm_random_graph(nodes, edges)
    directed_graph = nx.DiGraph()
    # for (u, v, w) in G.edges(data=True):
    #     G.edges[u, v]['weight'] = random.randint(1, 10)
    # print(G.edges(data=True))
    #print(G.nodes(data=True))
    directed_graph.add_nodes_from(G)
    directed_graph.add_edges_from(G.edges)

    for (u, v, w) in directed_graph.edges(data=True):
        directed_graph.edges[u, v]['weight'] = random.randint(1, 10)

    print(directed_graph.edges(data=True))

    # try:
    #     print(nx.shortest_path_length(directed_graph, 0, 4, 'weight'))
    # except nx.NetworkXNoPath:
    #     print('No path')
    #
    # print(list(directed_graph.successors(2)))
    #
    # print("cost    ", directed_graph[0][3]['weight'])

    return directed_graph


def SelectNode(probability):
    selected_node_type = np.random.choice(
        [0, 1],
        1,
        p=[probability, 1 - probability]
    )

    #print(selected_node_type)


if __name__ == '__main__':
    construct_graph(5, 10)
    SelectNode(0.4)


