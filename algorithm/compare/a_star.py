import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random
import time
import csv
"""
# G = nx.Graph()
# G.add_edge('x','a', capacity=3.0)
# G.add_edge('x','b', capacity=1.0)
# G.add_edge('a','c', capacity=3.0)
# G.add_edge('b','c', capacity=5.0)
# G.add_edge('b','d', capacity=4.0)
# G.add_edge('d','e', capacity=2.0)
# G.add_edge('c','y', capacity=2.0)
# G.add_edge('e','y', capacity=3.0)

# pos = nx.spring_layout(G)
# capacity = nx.get_edge_attributes(G, 'capacity')
# nx.draw_networkx_nodes(G, pos)
# nx.draw_networkx_edges(G, pos)
# nx.draw_networkx_labels(G, pos)
# nx.draw_networkx_edge_labels(G,pos,capacity)
# plt.show()
"""

def create_graph(data):
    G.add_weighted_edges_from(data)

def astar(start,terminal):
    cost = 0
    path = nx.astar_path(G, start, terminal)
    cost = nx.astar_path_length(G, start, terminal)
    # print("A Star Shortest Path: ")
    # for i in range(len(path)-1):
    #     print(path[i],"->",path[i+1])
    # print("Astar Shortest Path Cost: ",cost)
    

def draw():
    pos = nx.spring_layout(G)
    weight = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_nodes(G, pos,node_color='green',edge_color='orange',alpha=0.6)
    nx.draw_networkx_edges(G, pos,node_color='green',edge_color='orange',alpha=0.6)
    nx.draw_networkx_labels(G, pos,node_color='green',edge_color='orange')
    nx.draw_networkx_edge_labels(G,pos,weight,node_color='green',edge_color='orange')
    plt.axis('off')
    # plt.show()

def data_generator():

    data = [(0, 1, random.randint(1,10)), (0, 2, random.randint(1,10)), (0, 3, random.randint(1,10)), 
            (1, 0, random.randint(1,10)),(1, 3, random.randint(1,10)),(1, 4, random.randint(1,10)),
            (2, 0, random.randint(1,10)),(2, 3, random.randint(1,10)),(2, 5, random.randint(1,10)),
            (3, 0, random.randint(1,10)),(3, 1, random.randint(1,10)),(3, 2, random.randint(1,10)),(3, 4, random.randint(1,10)),(3, 5, random.randint(1,10)),(3, 6, random.randint(1,10)),
            (4, 1, random.randint(1,10)),(4, 3, random.randint(1,10)),(4, 6, random.randint(1,10)),
            (5, 2, random.randint(1,10)),(5, 3, random.randint(1,10)),(5, 6, random.randint(1,10)),
            (6, 3, random.randint(1,10)),(6, 4, random.randint(1,10)),(6, 5, random.randint(1,10))]
    return data
    # data = [(0, 1, 1), (0, 2, 2), (0, 3, 3), 
    #         (1, 0, 1),(1, 3, 2),(1, 4, 3),
    #         (2, 0, 2),(2, 3, 1),(2, 5, 4),
    #         (3, 0, 3),(3, 1, 2),(3, 2, 1),(3, 4, 1),(3, 5, 1),(3, 6, 1),
    #         (4, 1, 3),(4, 3, 1),(4, 6, 2),
    #         (5, 2, 4),(5, 3, 1),(5, 6, 2),
    #         (6, 3, 1),(6, 4, 2),(6, 5, 2)]

def get_start_terminal(data):

    m = sorted(data,key=lambda x:x[0])
    # print(m)
    length = len(m)
    start = m[0][0]
    terminal = m[length-1][0]
    return start,terminal


def storFile(data,fileName):
    with open(fileName,'w',newline ='') as f:
        mywrite = csv.writer(f)
        mywrite.writerow(data)
    

if __name__ == "__main__":
    

    counter = []
    
    for i in range(1000):

        start = time.clock()

        G=nx.Graph()                                    # create an object                                            
        get_data = data_generator()                     # create graph info
        create_graph(get_data)                          # create graph from the graph info
        get_s_t = get_start_terminal(get_data)          # default the start node and terminal node
        astar(get_s_t[0],get_s_t[1])                 # Djikstra Algorithm
    # time.sleep(2)
    # draw()
        end = time.clock()
        counter.append(end-start)
    

    # print(counter)
    # storFile(counter,'astar.csv')