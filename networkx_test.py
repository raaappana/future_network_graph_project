import networkx as nx
import matplotlib.pyplot as plt
#import nxviz

#make a graph
G = nx.Graph()
D = nx.DiGraph()
mult = nx.MultiGraph()

#edges can contain weights, ergo a singly weight metadata might denote 3

#Matrix plot
#nodes are row, collumns are
#collumns are matrix

#arc plot
#good for visualizing networks

#circos plot are circular arc plots
#nxviz is the


#self loops exist.

#add nodes to the graph with integer IDs
G.add_nodes_from([1,2,3,4,6])
print(G.nodes())

#Add an edge between nodes 1 and 2
#G.add_edge(1,2)
#G.add_edge(1,3)
#G.add_edge(2,3)

#adding a cycle to a network connects them all together in a loop
#G.add_cycle([2,3,6,1])
#Adding a path draws them in a line
#G.add_path([1,2,3])
#adding a star makes the first node the center, and all the other nodes "draw" from it
G.add_star([1,2,3,4,6])

print(G.edges())


G.node[1]['label'] = 'blue'
print (G.nodes(data=True))

nx.draw(G)
plt.show()
