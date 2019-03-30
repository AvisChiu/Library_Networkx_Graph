import networkx as nx
import matplotlib.pyplot as plt

#Create an empty graph with no nodes and no edges.
G = nx.Graph()
#Some methods of creating nodes and edges

#===1===#
G.add_node(1)
G.add_nodes_from([2, 3])
nx.draw_networkx(G,node_color='orange',node_size=200)

#===2===#
H = nx.path_graph(10)
G.add_nodes_from(H)
nx.draw_networkx(G,node_color='orange',node_size=200)

#===3===#
G.add_node("spam")                                      # adds node "spam", the node can be a string
G.add_nodes_from("spam")                                # adds 4 nodes: 's', 'p', 'a', 'm'
nx.draw_networkx(G,node_color='orange',node_size=200)

#==================draw the graph================# 
plt.axis('off')
plt.show()