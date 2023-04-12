import numpy as np
import igraph as ig
import random
import seaborn as sns
import matplotlib.pyplot as plt

### question 1 - part 1

def create_undirected_net(n = 900, p = 0.002, seed = 24):
    random.seed(seed)
    return ig.Graph.Erdos_Renyi(n = n, p = p, directed = False, loops = False)


    
