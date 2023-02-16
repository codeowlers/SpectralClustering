import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse import csr_matrix

def construct_matrices(X, k, sigma):
    """
    Constructs the weighted adjacency matrix W, degree matrix D, and Laplacian matrix L
    for a given set of data points using the k-nearest neighborhood approach and a Gaussian kernel
    with scaling parameter sigma.
    
    Args:
        X: np.ndarray of shape (n_samples, n_features) representing the data points
        k: int representing the number of nearest neighbors to consider
        sigma: float representing the scaling parameter for the Gaussian kernel
        
    Returns:
        W: sparse coo_matrix representing the weighted adjacency matrix
        D: sparse coo_matrix representing the degree matrix
        L: sparse coo_matrix representing the Laplacian matrix
    """
    n_samples = X.shape[0]
    pairwise_distances = np.sum(X**2, axis=1)[:, np.newaxis] + np.sum(X**2, axis=1) - 2*X.dot(X.T)
    pairwise_similarities = np.exp(-pairwise_distances / (2 * sigma**2))
    row_indices = np.arange(n_samples).repeat(k)
    kNN_indices = np.argpartition(-pairwise_distances, kth=k, axis=1)[:, :k]
    col_indices = kNN_indices.reshape(-1)
    similarities = pairwise_similarities[row_indices, col_indices]
    W = coo_matrix((similarities, (row_indices, col_indices)), shape=(n_samples, n_samples))
    degrees = np.asarray(W.sum(axis=1)).reshape(-1)
    D = coo_matrix((degrees, (np.arange(n_samples), np.arange(n_samples))), shape=(n_samples, n_samples))
    L = D - W
    return W, D, L


def construct_sparse_matrices(W):
    # Construct the degree matrix D
    D = np.diag(np.sum(W, axis=1))
    D_sparse = csr_matrix(D)

    # Construct the Laplacian matrix L
    L = D - W
    L_sparse = csr_matrix(L)

    # Convert the weighted adjacency matrix W to sparse format
    W_sparse = csr_matrix(W)

    return L_sparse, D_sparse, W_sparse
