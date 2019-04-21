import matplotlib.pyplot as plt
from matplotlib.pyplot import figure


def compare_by_time_and_node(x, y1, y2, y3):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Number of nodes')
    plt.ylabel('Run time (mSec)')
    plt.title('Comparison using total running time vs number of nodes')
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.legend(['OCL', 'A Star', 'Best First'], loc='upper left')
    plt.savefig("run_time_vs_nodes.eps")
    plt.show()


def compare_by_time_and_edge(x, y1, y2, y3):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Number of edges')
    plt.ylabel('Run time (mSec)')
    plt.title('Comparison using total running time vs number of edges')
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.legend(['OCL', 'A Star', 'Best First'], loc='upper left')
    plt.savefig("run_time_vs_edges.eps")
    plt.show()


def compare_by_expanded_node(x, y1, y2, y3):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Total number of nodes')
    plt.ylabel('Number of expanded nodes')
    plt.title('Comparison using total number of nodes vs number of expanded nodes')
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.legend(['OCL', 'A Star', 'Best First'], loc='upper left')
    plt.savefig("run_time_vs_expanded_nodes.eps")
    plt.show()


def compare_by_expanded_node_infinite(x, y1, y2, y3):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Total number of nodes')
    plt.ylabel('Number of expanded nodes')
    plt.title('Comparison using total number of nodes vs number of expanded nodes in infinite graph')
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.legend(['OCL', 'A Star', 'Best First'], loc='upper left')
    plt.savefig("nodes_vs_expanded_nodes_inf.eps")
    plt.show()


def compare_by_time_infinite(x, y1, y2, y3):
    figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')
    plt.xlabel('Total number of nodes')
    plt.ylabel('Run time (mSec)')
    plt.title('Comparison using total number of nodes vs runnning time in infinite graph')
    plt.grid(True)
    plt.plot(x, y1, color='y', linestyle='-', marker='.')
    plt.plot(x, y2, color='g', linestyle='--', marker='.')
    plt.plot(x, y3, color='r', linestyle=':', marker='.')
    plt.legend(['OCL', 'A Star', 'Best First'], loc='upper left')
    plt.savefig("run_time_vs_nodes_inf.eps")
    plt.show()
