import networkx as nx


def construct_graph1(nodes, edges):
    directed_graph = nx.DiGraph()

    for i in range(13):
        directed_graph.add_node(i)

    directed_graph.add_edge(0, 1)
    directed_graph.add_edge(0, 2)
    directed_graph.add_edge(1, 3)
    directed_graph.add_edge(1, 4)
    directed_graph.add_edge(3, 7)
    directed_graph.add_edge(3, 8)
    directed_graph.add_edge(4, 9)
    directed_graph.add_edge(2, 5)
    directed_graph.add_edge(2, 6)
    directed_graph.add_edge(5, 12)
    directed_graph.add_edge(6, 10)
    directed_graph.add_edge(6, 11)

    directed_graph.edges[0, 1]['weight'] = 2
    directed_graph.edges[0, 2]['weight'] = 1
    directed_graph.edges[1, 3]['weight'] = 3
    directed_graph.edges[1, 4]['weight'] = 2
    directed_graph.edges[3, 7]['weight'] = 9
    directed_graph.edges[3, 8]['weight'] = 8
    directed_graph.edges[4, 9]['weight'] = 6
    directed_graph.edges[2, 5]['weight'] = 4
    directed_graph.edges[2, 6]['weight'] = 1
    directed_graph.edges[5, 12]['weight'] = 4
    directed_graph.edges[6, 10]['weight'] = 5
    directed_graph.edges[6, 11]['weight'] = 6

    print(directed_graph.edges(data=True))

    return directed_graph


if __name__ == '__main__':
    construct_graph1(5, 10)
