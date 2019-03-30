import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
H = nx.path_graph(10)
G.add_nodes_from(H)
# already created nodes

# create edges
G.add_edge(1, 2)                        # method 1            
e = (2, 3)                              # method 2
G.add_edge(*e)                          # unpack edge tuple*
G.add_edges_from([(1, 2), (3, 4)])      # method 3 :using list to add edges
G.add_edges_from(H.edges)               # method 4 :add edges at the same time

G.add_node("string")                    # adds node "spam", the node can be a string
G.add_nodes_from("string")              # adds 4 nodes: 's', 'p', 'a', 'm'
G.add_edge(3, 'g')

print(G.number_of_nodes())
print(G.number_of_edges())
print(list(G.nodes))
print(list(G.edges))
print(list(G.adj[1]))                   # or list(G.neighbors(1)) , node 1's neighbors
print(G.degree[1])                      # the number of edges incident to 1

print(G.edges([2, 'g']))                # show the edges which 2 (g) connect to    
print(G.edges([2, 'g', 3, 4, 5]))
print(G.degree([2, 3]))                 # the number of edges incident to 2 ,3
print(G.degree([2, 3, 4, 5]))


print(G[1])                             # same as G.adj[1]
print(G[1][2])
print(G.edges[1, 2])

#==================draw the graph================# 
nx.draw_networkx(G,node_color='orange',node_size=200)
plt.axis('off')
plt.show()

G.clear()                               # delete the graph and will show nothing