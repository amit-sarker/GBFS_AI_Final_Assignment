import random

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def construct_infinite_graph(nodes):
    directed_graph = nx.DiGraph()

    for i in range(nodes):
        directed_graph.add_node(i)

    directed_graph.add_edge(0, 1)
    directed_graph.add_edge(0, nodes - 2)
    directed_graph.add_edge(nodes - 2, nodes - 1)

    for i in range(1, nodes - 3):
        directed_graph.add_edge(i, i+1)

    directed_graph.add_edge(nodes - 3, nodes - 1)

    directed_graph.edges[0, 1]['weight'] = 1
    directed_graph.edges[0, nodes - 2]['weight'] = 1000000
    directed_graph.edges[nodes - 2, nodes - 1]['weight'] = 500000

    directed_graph.edges[nodes - 3, nodes - 1]['weight'] = 1

    for i in range(1, nodes - 3):
        directed_graph.edges[i, i+1]['weight'] = 1

    print(directed_graph.edges(data=True))
    return directed_graph
