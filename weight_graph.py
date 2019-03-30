import networkx as nx
import matplotlib.pyplot as plt


def method_1():

    # structure of dictionary of dictionary of dictionary
    for node, neighbor in FG.adj.items():
        # print(node)
        # print(neighbor)
        # print(neighbor.items())
        for nbr, weight in neighbor.items():                         # structure of dictionary of dictionary
            wt = weight['weight']
            if wt < 0.5:
                print('(%d, %d, %.3f)' % (node, nbr, wt))            # undirected graphs, adjacency iteration sees each edge twice.

    print("=========================================")

    # structure of dictionary of dictionary of dictionary
    for node, neighbor in FG.adj.items():
        # print(node)
        # print(neighbor)
        # print(neighbor.items())
        for nbr, weight in neighbor.items():                      # structure of dictionary of dictionary
            wt = weight['weight']
            print('(%d, %d, %.3f)' % (node, nbr, wt))

def method_2():

    for (u, v, wt) in FG.edges.data('weight'):
        if wt < 0.5:
            print('(%d, %d, %.3f)' % (u, v, wt))

    print("=========================================")

    for (u, v, wt) in FG.edges.data('weight'):
        print('(%d, %d, %.3f)' % (u, v, wt))



if __name__ == "__main__":

    FG = nx.Graph()
    FG.add_weighted_edges_from([(1, 2, 0.125), (1, 3, 0.75), (2, 4, 1.2), (3, 4, 0.375)])
    print(list(FG.nodes))
    print(list(FG.edges))
    print(FG.adj.items())
    print("\n\n")
    
    print("method1")
    method_1()
    print("method2")
    method_2()

    # nx.draw_networkx(FG, node_color='orange', node_size=200)
    # plt.axis('off')
    # plt.show()
    # FG.clear()                               # delete the graph and will show nothing
