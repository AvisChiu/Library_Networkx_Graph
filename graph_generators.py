#!/usr/bin/python
#coding:utf-8
"""
Applying classic graph operations, such as:

subgraph(G, nbunch)      - induced subgraph view of G on nodes in nbunch
union(G1,G2)             - graph union
disjoint_union(G1,G2)    - graph union assuming all nodes are different
cartesian_product(G1,G2) - return Cartesian product graph
compose(G1,G2)           - combine graphs identifying nodes common to both
complement(G)            - graph complement
create_empty_copy(G)     - return an empty copy of the same graph class
to_undirected(G) - return an undirected representation of G
to_directed(G)   - return a directed representation of G

"""

import matplotlib.pyplot as plt
import networkx as nx


# In fact, the graph type can be defined by self.
# perterson, tuttle...are just some examples
# Using a call to one of the classic small graphs, e.g.,
petersen = nx.petersen_graph()
tutte = nx.tutte_graph()
maze = nx.sedgewick_maze_graph()
tet = nx.tetrahedral_graph()

# Using a (constructive) generator for a classic graph, e.g.,
K_5 = nx.complete_graph(5)
K_3_5 = nx.complete_bipartite_graph(3, 5)
barbell = nx.barbell_graph(10, 10)
lollipop = nx.lollipop_graph(10, 20)

# operator
new = nx.to_directed(lollipop)

# Using a stochastic graph generator, e.g.,
er = nx.erdos_renyi_graph(10, 0.15)
ws = nx.watts_strogatz_graph(30, 3, 0.1)
ba = nx.barabasi_albert_graph(10, 5)
red = nx.random_lobster(10, 0.9, 0.9)

# write to file / load graph from file
nx.write_gml(red, "path.to.file")
mygraph = nx.read_gml("path.to.file")


nx.draw_networkx(mygraph)
plt.axis('off')
plt.show()

