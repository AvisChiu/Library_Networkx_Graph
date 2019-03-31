# Add node attributes 
# using add_node(), 
# add_nodes_from(), 
# or G.nodes

import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_node(1, client='client1')                           # add node 1 with attribute time="5pm"
G.add_node(2)
G.add_nodes_from([3], client='client2')
G.add_node(4, client="3pm")

print(G.nodes[1])                                   # it means print node 1's attributes
print(G.nodes[2])                                   # node 2 has nothing of any attributes, so print : {}


G.nodes[1]['load'] = 1000                           
print(G.nodes[1])                                   # print node 1's attributes
print(G.nodes.data())                               # print all s attributes



nx.draw_networkx(G, node_color='orange', node_size=200)
plt.axis('off')
plt.show()