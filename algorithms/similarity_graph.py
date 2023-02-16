import numpy as np
from scipy.spatial.distance import cdist

# k represents the number of clusters that we want to identify in the data
# sigma (σ) is a parameter that controls the width of the Gaussian kernel used to compute the pairwise similarities between data points
def construct_similarity_graph(X, k, sigma):
    # Compute the pairwise similarity matrix
    S = np.exp(-cdist(X, X, 'sqeuclidean') / (2 * sigma ** 2))

    # Construct the adjacency matrix
    W = np.zeros((len(X), len(X)))
    for i in range(len(X)):
        dists = [(j, S[i, j]) for j in range(len(X)) if j != i]
        dists.sort(key=lambda x: x[1])
        for j, _ in dists[:k]:
            W[i, j] = S[i, j]
            W[j, i] = S[j, i]

    # Set the diagonal elements of W to 0
    np.fill_diagonal(W, 0)

    return W
