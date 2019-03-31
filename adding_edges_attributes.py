# Add/change edge attributes 
# using add_edge(), 
# add_edges_from(), 
# or subscript notation.
import matplotlib.pyplot as plt
import networkx as nx

def add_nodes():
    
    G.add_node(1, client='client1')                             # add node 1 with attribute time="5pm"
    G.add_node(2, client='client2')
    G.add_nodes_from([3], client='client3')
    G.add_node(4, client="client4")
    G.nodes[1]['load'] = 1000           
    G.nodes[2]['load'] = 1000    
    G.nodes[3]['load'] = 1000    
    G.nodes[4]['load'] = 1000    
    print(G.nodes.data())                                       # print all s attributes

def add_edges():

    G.add_edge(1, 2, distance=1.0 )
    # G.add_edges_from([(3, 4), (4, 5)],distance=5.5)             # batch 
    G.add_edge(2, 3, distance=2.0 )
    G.add_edge(3, 4, distance=3.0 )
    G.add_edge(4, 5, distance=4.0 )
    print(G.edges.data())

    G[1][2]['distance'] = 5.0
    G[2][3]['distance'] = 6.0
    G[3][4]['distance'] = 7.0
    G[4][5]['distance'] = 8.0
    print(G.edges.data())

    G.edges[1, 2]['distance'] = 9.0
    G.edges[2, 3]['distance'] = 10.0
    G.edges[3, 4]['distance'] = 11.0
    G.edges[4, 5]['distance'] = 12.0
    G.edges[4, 5]['other'] = "nothing"                          # add another edge's attribute
    print(G.edges.data())

def draw():

    nx.draw_networkx(G)
    plt.axis('off')
    plt.show()


if __name__ == "__main__":

    G = nx.Graph()
    # add_nodes()
    add_edges()
    draw()