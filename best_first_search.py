import random

from Graph_Construction import construct_graph
from decimal import Decimal
import networkx as nx
import numpy as np
import operator

from test import construct_graph1


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


def SelectNode(open, h_values, g_values):
    f_list = []
    print("Open        ", open)
    for val in open:
        f_list.append(h_values.get(val))
    min_f_val = min(f_list)
    index = f_list.index(min_f_val)

    if min_f_val != Decimal('Infinity'):
        return open[index]
    return -1


def best_first_algo(graph, goal):
    parent = {}
    open = []
    closed = []
    #goal_node = 49

    #graph = construct_graph(number_of_nodes, number_of_edges)
    g_values = calculate_g_values(graph)
    h_values = calculate_h_values(graph, goal)
    print("G Vals:    ", g_values)
    print("h Vals:    ", h_values)

    parent.update({0: 'none'})
    open.append(0)
    print('\n')

    while open.__len__() != 0:
        n = SelectNode(open, h_values, g_values)
        if n == -1:
            return []
        print("Node selected   ", n)
        open.remove(n)
        if n == goal:
            closed.append(goal)
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


# if __name__ == '__main__':
#     # print("Enter Number of Nodes of the graph: ")
#     # number_of_nodes = int(input())
#     # print("Enter Number of Edges of the graph: ")
#     # number_of_edges = int(input())
#     # OCL_Algo(number_of_nodes, number_of_edges)
#     result = best_first_algo(50, 100)
#
#     if len(result) == 0:
#         print("No solution exist")
#     else:
#         print("Resultant Path:  ", result)
