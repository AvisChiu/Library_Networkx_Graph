# Attributes such as weights, labels, colors, or whatever Python object you like, 
# can be attached to graphs, nodes, or edges.
# Each graph, node, and edge can hold key/value attribute pairs in an associated attribute dictionary (the keys must be hashable).
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph(day="Friday",month="Jan")
print(G.graph)
print(G.graph['day'])                           # index 'day'

G.graph['day'] = "Monday"                       # change the attribute
print(G.graph)              


nx.draw_networkx(G, node_color='orange', node_size=200)
plt.axis('off')
plt.show()
