#!/usr/bin/python
#coding:utf-8
"""
NetworkX provides classes for graphs which allow multiple edges between any pair of nodes. 
The --> MultiGraph <--  and --> MultiDiGraph <--  classes allow you to add the same edge twice, possibly with different edge data. 
This can be powerful for some applications, but many algorithms are not well defined on such graphs. 
Where results are well defined, 

e.g., MultiGraph.degree() we provide the function. 

Otherwise you should convert to a standard graph in a way that makes the measurement well defined.

"""

import matplotlib.pyplot as plt
import networkx as nx

MG = nx.MultiGraph()
MG.add_weighted_edges_from([(1, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5)])

print(MG.degree())                                                      # the number of edges of each node
print(MG.degree(weight='weight'))                                       # each node's total degree
print(MG.degree(1, weight='weight'))                                    # node 1's total degree
print(dict(MG.degree(weight='weight')))                                 # # each node's total degree in a dictionary


GG = nx.Graph()
for nodes, neighbor in MG.adjacency():
    # print(nodes)                                    # node and neighbor structure
    # print(neighbor)                                 # (1, AdjacencyView({2: {0: {'weight': 0.5}, 1: {'weight': 0.75}}})), 
    # print(MG.adj.items())                           # (2, AdjacencyView({1: {0: {'weight': 0.5}, 1: {'weight': 0.75}},3: {0: {'weight': 0.5}}})), 
                                                    # (3, AdjacencyView({2: {0: {'weight': 0.5}}}))
    for nbr, edict in neighbor.items():
        minvalue = min([d['weight'] for d in edict.values()])       # 一對 node 之間的 edge 可以有很多個 weight ，選最小的 weight
        GG.add_edge(nodes, nbr, weight = minvalue)


print(GG.degree(weight='weight'))

nx.shortest_path(GG, 1, 3)                              # default BFS: node 1-->3 's shortest path
nx.draw_networkx(GG)
plt.axis('off')
plt.show()