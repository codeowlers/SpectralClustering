import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering

def agglomerative_clustering(X, n_clusters, title):

    # Initialize and fit the Agglomerative Clustering model to the data
    agg_clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    labels = agg_clustering.fit_predict(X)

    # Plot the results
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
    plt.title(f'{title}')
    plt.show()
    
    return labels