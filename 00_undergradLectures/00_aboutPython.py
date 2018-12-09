# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 23:16:15 2018

@author: manma
"""

import numpy as np
from scipy.stats import norm
from scipy.integrate import quad
import pandas as pd

# %% Numpy
a = np.linspace(-np.pi, np.pi, 100)
b = np.cos(a)
c = np.sin(a)
print(b @ c)

# %% Scipy
ϕ = norm()
value, error = quad(ϕ.pdf, -2, 2)
print(value)

# %% Pandas
np.random.seed(1234)

data = np.random.rand(5, 2)
dates = pd.date_range('28/12/2010', periods=5)

df = pd.DataFrame(data, columns=['price', 'weight'], index=dates)

print(df.mean())

# %% Networkx
import networkx as nx
import matplotlib.pyplot as plt
np.random.seed(1234)

# Generate random graph
p = dict((i,(np.random.uniform(0, 1), 
             np.random.uniform(0, 1))) for i in range(200))
G = nx.random_geometric_graph(200, 0.12, pos=p)
pos = nx.get_node_attributes(G, 'pos')

# find node nearest the center point (0.5, 0.5)
dists = [(x - 0.5)**2 + (y - 0.5)**2 for x, y in list(pos.values())]
ncenter = np.argmin(dists)

# Plot graph, coloring by path length from central node
p = nx.single_source_shortest_path_length(G, ncenter)
plt.figure()
nx.draw_networkx_edges(G, pos, alpha=0.4)
nx.draw_networkx_nodes(G,
                       pos,
                       nodelist=list(p.keys()),
                       node_size=120, alpha=0.5,
                       node_color=list(p.values()),
                       cmap=plt.cm.jet_r)
plt.show()
