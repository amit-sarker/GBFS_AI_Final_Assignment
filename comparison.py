import time

from math import ceil

from Graph_Construction import construct_graph
from OCL_Framework import OCL_Algo
from a_star_search import a_star_algo
from best_first_search import best_first_algo
from comparison_graph import compare_by_time_and_node, compare_by_time_and_edge, compare_by_expanded_node, \
    compare_by_expanded_node_infinite, compare_by_time_infinite
from infinite_graph_construction import construct_infinite_graph


def single_run():
    total_nodes = 5
    total_edges = 10
    goal_node = total_nodes - 1
    graph = construct_graph(total_nodes, total_edges)

    start_ocl = time.time()
    result_ocl = OCL_Algo(graph, goal_node)
    end_ocl = time.time()
    elapsed_ocl = (end_ocl - start_ocl) * 1000
    print("Elapsed time OCL:   ", elapsed_ocl)
    print('\n')

    start_astar = time.time()
    result_astar = a_star_algo(graph, goal_node)
    end_astar = time.time()
    elapsed_astar = (end_astar - start_astar) * 1000
    print("Elapsed time aStar:   ", elapsed_astar)
    print('\n')

    start_best_first = time.time()
    result_best_first = best_first_algo(graph, goal_node)
    end_best_first = time.time()
    elapsed_best_first = (end_best_first - start_best_first) * 1000
    print("Elapsed time best first:   ", elapsed_best_first)
    print('\n')


def compare_infinite_graph():
    total_nodes = 1004
    graph = construct_infinite_graph(total_nodes)
    goal_node = total_nodes - 1

    result_ocl = OCL_Algo(graph, goal_node)
    nodes_ocl = result_ocl.__len__()

    result_astar = a_star_algo(graph, goal_node)
    nodes_astar = result_astar.__len__()

    result_best_first = best_first_algo(graph, goal_node)
    nodes_best_first = result_best_first.__len__()

    print(result_ocl)
    print(result_astar)
    print(result_best_first)

    print("OCL:  ", nodes_ocl)
    print("A star:  ", nodes_astar)
    print("Best first:  ", nodes_best_first)


def comp_by_infinite_time():
    total_nodes = 100
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_nodes >= 1000:
            break
        goal_node = total_nodes - 1
        time1 = 0
        time2 = 0
        time3 = 0

        for i in range(200):
            graph = construct_infinite_graph(total_nodes)

            start_ocl = time.time()
            result_ocl = OCL_Algo(graph, goal_node)
            end_ocl = time.time()
            elapsed_ocl = (end_ocl - start_ocl) * 1000

            start_astar = time.time()
            result_astar = a_star_algo(graph, goal_node)
            end_astar = time.time()
            elapsed_astar = (end_astar - start_astar) * 1000

            start_best_first = time.time()
            result_best_first = best_first_algo(graph, goal_node)
            end_best_first = time.time()
            elapsed_best_first = (end_best_first - start_best_first) * 1000

            time1 += elapsed_ocl
            time2 += elapsed_astar
            time3 += elapsed_best_first

        x.append(total_nodes)
        y1.append(time1 / 200)
        y2.append(time2 / 200)
        y3.append(time3 / 200)

        total_nodes += 100

    compare_by_time_infinite(x, y1, y2, y3)


def comp_by_infinite_graph():
    total_nodes = 100
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_nodes >= 1000:
            break
        goal_node = total_nodes - 1
        nodes1 = 0
        nodes2 = 0
        nodes3 = 0

        for i in range(200):
            graph = construct_infinite_graph(total_nodes)

            result_ocl = OCL_Algo(graph, goal_node)
            nodes_ocl = result_ocl.__len__()

            result_astar = a_star_algo(graph, goal_node)
            nodes_astar = result_astar.__len__()

            result_best_first = best_first_algo(graph, goal_node)
            nodes_best_first = result_best_first.__len__()

            nodes1 += nodes_ocl
            nodes2 += nodes_astar
            nodes3 += nodes_best_first

        x.append(total_nodes)
        y1.append(nodes1 / 200)
        y2.append(nodes2 / 200)
        y3.append(nodes3 / 200)

        total_nodes += 100

    compare_by_expanded_node_infinite(x, y1, y2, y3)


def comp_by_total_expanded_nodes():
    total_nodes = 5
    x = []
    y1 = []
    y2 = []
    y3 = []

    f_ocl = open("f_ocl_nodes_ex.txt", "w")
    f_astar = open("f_astar_nodes_ex.txt", "w")
    f_best = open("f_best_nodes_ex.txt", "w")

    while True:
        if total_nodes >= 500:
            break
        total_edges = 3 * total_nodes
        goal_node = total_nodes - 1
        nodes1 = 0
        nodes2 = 0
        nodes3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            result_ocl = OCL_Algo(graph, goal_node)
            nodes_ocl = result_ocl.__len__()

            result_astar = a_star_algo(graph, goal_node)
            nodes_astar = result_astar.__len__()

            result_best_first = best_first_algo(graph, goal_node)
            nodes_best_first = result_best_first.__len__()

            nodes1 += nodes_ocl
            nodes2 += nodes_astar
            nodes3 += nodes_best_first

        x.append(total_nodes)
        y1.append(nodes1 / 200)
        y2.append(nodes2 / 200)
        y3.append(nodes3 / 200)

        for i in range(len(y1)):
            f_ocl.write(str(y1[i]))
            f_ocl.write('\n')
            f_astar.write(str(y2[i]))
            f_astar.write('\n')
            f_best.write(str(y3[i]))
            f_best.write('\n')

        if total_nodes < 50:
            total_nodes += 5
        elif total_nodes < 200:
            total_nodes += 10
        elif total_nodes < 350:
            total_nodes += 30
        else:
            total_nodes += 50

        if total_nodes == 50:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 200:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 350:
            compare_by_expanded_node(x, y1, y2, y3)
        elif total_nodes == 500:
            compare_by_expanded_node(x, y1, y2, y3)


def comp_by_nodes_time():
    total_nodes = 5
    x = []
    y1 = []
    y2 = []
    y3 = []
    f_ocl = open("f_ocl_nodes.txt", "w")
    f_astar = open("f_astar_nodes.txt", "w")
    f_best = open("f_best_nodes.txt", "w")

    while True:
        if total_nodes >= 500:
            break
        total_edges = 3 * total_nodes
        goal_node = total_nodes - 1
        time1 = 0
        time2 = 0
        time3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            start_ocl = time.time()
            result_ocl = OCL_Algo(graph, goal_node)
            end_ocl = time.time()

            elapsed_ocl = end_ocl - start_ocl
            print("elapsed OCL:   ", elapsed_ocl)

            start_astar = time.time()
            result_astar = a_star_algo(graph, goal_node)
            end_astar = time.time()

            elapsed_astar = end_astar - start_astar
            print("elapsed aStar:   ", elapsed_astar)

            start_best_first = time.time()
            result_best_first = best_first_algo(graph, goal_node)
            end_best_first = time.time()

            elapsed_best_first = end_best_first - start_best_first
            print("elapsed best first:   ", elapsed_best_first)

            time1 += elapsed_ocl
            time2 += elapsed_astar
            time3 += elapsed_best_first
        x.append(total_nodes)
        y1.append(time1 / 200)
        y2.append(time2 / 200)
        y3.append(time3 / 200)



        if total_nodes < 50:
            total_nodes += 5
        elif total_nodes < 200:
            total_nodes += 10
        elif total_nodes < 350:
            total_nodes += 30
        else:
            total_nodes += 50

        if total_nodes == 50:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 200:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 350:
            compare_by_time_and_node(x, y1, y2, y3)
        elif total_nodes == 500:
            compare_by_time_and_node(x, y1, y2, y3)


def comp_by_edges_time():
    total_edges = 15
    x = []
    y1 = []
    y2 = []
    y3 = []

    while True:
        if total_edges >= 2000:
            break
        total_nodes = ceil(total_edges / 3)
        goal_node = total_nodes - 1
        time1 = 0
        time2 = 0
        time3 = 0

        for i in range(200):
            graph = construct_graph(total_nodes, total_edges)

            start_ocl = time.time()
            result_ocl = OCL_Algo(graph, goal_node)
            end_ocl = time.time()

            elapsed_ocl = end_ocl - start_ocl
            print("elapsed OCL:   ", elapsed_ocl)

            start_astar = time.time()
            result_astar = a_star_algo(graph, goal_node)
            end_astar = time.time()

            elapsed_astar = end_astar - start_astar
            print("elapsed aStar:   ", elapsed_astar)

            start_best_first = time.time()
            result_best_first = best_first_algo(graph, goal_node)
            end_best_first = time.time()

            elapsed_best_first = end_best_first - start_best_first
            print("elapsed best first:   ", elapsed_best_first)

            time1 += elapsed_ocl
            time2 += elapsed_astar
            time3 += elapsed_best_first
        x.append(total_edges)
        y1.append(time1 / 200)
        y2.append(time2 / 200)
        y3.append(time3 / 200)

        if total_edges < 150:
            total_edges += 15
        elif total_edges < 600:
            total_edges += 30
        elif total_edges < 1050:
            total_edges += 90
        else:
            total_edges += 150

        if total_edges == 200:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges == 600:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges == 1000:
            compare_by_time_and_edge(x, y1, y2, y3)
        elif total_edges >= 2000:
            compare_by_time_and_edge(x, y1, y2, y3)
