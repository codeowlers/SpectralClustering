from scipy.sparse import dok_matrix
import numpy as np

def construct_similarity_graph(X, k, sigma):
    # Extract only the first two columns of X
    X = X[:, :2]

    # Initialize a sparse adjacency matrix
    N = len(X)
    W = dok_matrix((N, N), dtype=float)

    # Compute similarity for each point
    for i in range(N):
        # Compute similarity with every other point
        diff = X - X[i]
        sim = np.exp(-np.sum(diff ** 2, axis=1) / (2 * sigma ** 2))
        sim[i] = 0  # Set similarity with itself to 0
        top_k_idx = np.argsort(-sim)[:k]  # Get the indices of the K most similar points
        top_k_sim = sim[top_k_idx]  # Get the similarity values of the K most similar points
        W[i, top_k_idx] = top_k_sim  # Set values of the adjacency matrix
        W[top_k_idx, i] = top_k_sim

    # Set the diagonal elements of W to 0
    W.setdiag(0)

    return W.toarray()