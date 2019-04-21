import random
from decimal import Decimal

import networkx as nx
import numpy as np


def calculate_g_values(graph):
    g_values = {}
    for node in graph.node():
        try:
            g_values.update({node: nx.shortest_path_length(graph, 0, node, 'weight')})
        except nx.NetworkXNoPath:
            g_values.update({node: Decimal('Infinity')})
    return g_values


def calculate_h_values(graph, destination):
    h_values = {}
    for node in graph.node():
        try:
            h_values.update({node: nx.shortest_path_length(graph, node, destination, 'weight')})
        except nx.NetworkXNoPath:
            h_values.update({node: Decimal('Infinity')})
    return h_values


def select_node_with_min_h(open, h_values):
    h_list = []
    for val in open:
        h_list.append(h_values.get(val))
    min_h_val = min(h_list)
    index = h_list.index(min_h_val)
    if min_h_val != Decimal('Infinity'):
        return open[index]
    return -1


def select_random_node(open):
    return open[random.randint(0, len(open) - 1)]


def SelectNode(open, probability, h_values):
    selected_node_type = np.random.choice(
        [0, 1],
        1,
        p=[1 - probability, probability]
    )
    if selected_node_type[0] == 0:
        return select_node_with_min_h(open, h_values)
    else:
        return select_random_node(open)


def OCL_Algo(graph, goal):
    parent = {}
    open = []
    closed = []
    probability = 0.8

    g_values = calculate_g_values(graph)
    h_values = calculate_h_values(graph, goal)
    print("G Vals:    ", g_values)
    print("h Vals:    ", h_values)

    parent.update({0: 'none'})
    open.append(0)

    while open.__len__() != 0:
        n = SelectNode(open, probability, h_values)
        if n == -1:
            return []
        print("Node selected   ", n)
        open.remove(n)
        if n == goal:
            closed.append(goal)
            if len(closed) == 0:
                print("No solution exist (OCL)")
            else:
                print("Expanded Path nodes (OCL):  ", closed)
            return closed

        for child in graph.successors(n):
            if child in open:
                if g_values.get(n) + graph[n][child]['weight'] < g_values.get(child):
                    g_values.update({child: g_values.get(n) + graph[n][child]['weight']})
                    parent.update({child: n})
            elif child in closed:
                if g_values.get(n) + graph[n][child]['weight'] < g_values.get(child):
                    g_values.update({child: g_values.get(n) + graph[n][child]['weight']})
                    parent.update({child: n})
                    closed.remove(child)
                    open.append(child)
            else:
                g_values.update({child: g_values.get(n) + graph[n][child]['weight']})
                parent.update({child: n})
                open.append(child)
        closed.append(n)
    return []
