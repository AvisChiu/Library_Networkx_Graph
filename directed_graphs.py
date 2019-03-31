"""
The DiGraph class provides additional properties specific to directed edges, 

e.g., 
DiGraph.out_edges(), 
DiGraph.in_degree(), 
DiGraph.predecessors(), 
DiGraph.successors() etc. 

To allow algorithms to work with both classes easily, 
the directed versions of neighbors() is equivalent to successors() while degree reports the sum of in_degree and out_degree 
even though that may feel inconsistent at times.

Note : In digraph, succesors is equal to neighbor

"""

import matplotlib.pyplot as plt
import networkx as nx

def DiGraph():

    DG = nx.DiGraph()
    DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])             # (start , end , weight)

    print(DG.in_degree(1, weight='weight'))                             # node 1's in_degree weight
    print(DG.out_degree(1, weight='weight'))                            # node 1's out_degree weight
    print(DG.degree(1, weight='weight'))                                # node 1's all degree weight

    print(list(DG.successors(3)))                                       # node 3's succesors is node 1
    print(list(DG.neighbors(1)))                                        # node 1's succesors/neighbor is node 2

    nx.draw_networkx(DG)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    
    DiGraph()