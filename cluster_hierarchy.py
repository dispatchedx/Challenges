import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

X = np.array([[0,0,0,0,0,0],
    [0.24,0,0,0,0,0],
    [0.22,0.15,0,0,0,0],
    [0.37,0.20,0.15,0,0,0],
    [0.34,.014,0.28,0.29,0,0],
    [0.23,0.25,0.11,0.22,0.39,0]
])
X = np.array([  [0, 0.71, 5.66, 3.61, 4.24, 3.20],
                [0.71, 0, 4.95, 2.92, 3.54, 2.50],
                [5.66, 4.95, 0, 2.24, 1.41, 2.50],
                [3.61, 2.92, 2.24, 0, 1.0, 0.50],
                [4.24, 3.54, 1.41, 1.0, 0, 1.12],
                [3.20, 2.50, 2.50, 0.50, 1.12, 0]
])


linked = linkage(X, 'single')

labelList = ["p1","p2","p3","p4","p5","p6"]
labelList = ["A","B","C","D","E","F"]
plt.figure(figsize=(10, 7))
dendrogram(linked,
            orientation='top',
            labels=labelList,
            distance_sort='ascending',
            show_leaf_counts=True)

plt.show()