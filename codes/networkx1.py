import os
import networkx as nx
import matplotlib.pyplot as plt


dir_name='C:\\Users\\Saumya\\Desktop\\smni_eeg_data\\a_m_co2a0000364'

os.chdir(dir_name)

data_a1 = [(29,30),(31,62),(57,58),(57,59),(29,58)]
labels_a1 = {(29,30):1,(31,62):2,(57,58):2,(57,59):3,(29,58):2}

data_am = [(44,47),(31,62),(38,62),(29,58),(4,6),(59,60)]
labels_am = {(44,47):1,(31,62):3,(38,62):1,(29,58):2,(4,6):2,(59,60):1}

data_an = [(31,62),(57,58),(44,47),(57,58),(29,58)]
labels_an = {(31,62):4,(57,58):2,(44,47):1,(57,58):1,(29,58):2}

data_c1 = [(22,28),(20,48),(23,27),(1,5),(21,23),(29,30),(23,51)]
labels_c1 = {(22,28):1,(20,48):1,(23,27):1,(1,5):4,(21,23):1,(29,30):1,(23,51):1}

data_cm = [(1,31),(1,5),(50,60),(1,33),(43,47),(4,5),(22,28)]
labels_cm = {(1,31):1,(1,5):3,(50,60):1,(1,33):2,(43,47):1,(4,5):1,(22,28):1}

data_cn = [(1,33),(1,5),(22,28),(29,58)]
labels_cn = {(1,33):2,(1,5):3,(22,28):2,(29,58):3}

G1=nx.Graph()
fig = plt.figure()

ax = fig.add_subplot(3,2,1)
ax.set_title("a1")
for c in data_a1:
    G1.add_edge(c[0],c[1])

pos = nx.spring_layout(G1)
nx.draw_networkx_nodes(G1,pos)
nx.draw_networkx_labels(G1,pos)
nx.draw_networkx_edges(G1,pos,edge_color='b')
nx.draw_networkx_edge_labels(G1,pos,edge_labels=labels_a1)
plt.axis('off')

G2 = nx.Graph()
ax = fig.add_subplot(3,2,2)
ax.set_title("am")
for c in data_am:
    G2.add_edge(c[0],c[1])

pos = nx.spring_layout(G2)
nx.draw_networkx_nodes(G2,pos)
nx.draw_networkx_labels(G2,pos)
nx.draw_networkx_edges(G2,pos,edge_color='g')
nx.draw_networkx_edge_labels(G2,pos,edge_labels=labels_am)
plt.axis('off')

G3 = nx.Graph()
ax = fig.add_subplot(3,2,3)
ax.set_title("an")
for c in data_an:
    G3.add_edge(c[0],c[1])

pos = nx.spring_layout(G3)
nx.draw_networkx_nodes(G3,pos)
nx.draw_networkx_labels(G3,pos)
nx.draw_networkx_edges(G3,pos,edge_color='y')
nx.draw_networkx_edge_labels(G3,pos,edge_labels=labels_an)
plt.axis('off')

G4 = nx.Graph()
ax = fig.add_subplot(3,2,4)
ax.set_title("c1")
for c in data_c1:
    G4.add_edge(c[0],c[1])

pos = nx.spring_layout(G4)
nx.draw_networkx_nodes(G4,pos)
nx.draw_networkx_labels(G4,pos)
nx.draw_networkx_edges(G4,pos,edge_color='b')
nx.draw_networkx_edge_labels(G4,pos,edge_labels=labels_c1)
plt.axis('off')

G5 = nx.Graph()
ax = fig.add_subplot(3,2,5)
ax.set_title("cm")
for c in data_cm:
    G5.add_edge(c[0],c[1])

pos = nx.spring_layout(G5)
nx.draw_networkx_nodes(G5,pos)
nx.draw_networkx_labels(G5,pos)
nx.draw_networkx_edges(G5,pos,edge_color='g')
nx.draw_networkx_edge_labels(G5,pos,edge_labels=labels_cm)
plt.axis('off')

G6 = nx.Graph()
ax = fig.add_subplot(3,2,6)
ax.set_title("cn")
for c in data_cn:
    G6.add_edge(c[0],c[1])

pos = nx.spring_layout(G6)
# try random, spectral, circular
nx.draw_networkx_nodes(G6,pos)
nx.draw_networkx_labels(G6,pos)
nx.draw_networkx_edges(G6,pos,edge_color='y')
nx.draw_networkx_edge_labels(G6,pos,edge_labels=labels_cn)
#nx.draw_networkx(G)
plt.axis('off')
plt.show()
