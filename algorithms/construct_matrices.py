import numpy as np
from scipy.sparse import csr_matrix

import numpy as np
from scipy.sparse import csr_matrix

def construct_laplacian(W):
    # Construct the degree matrix D
    D = np.diag(np.sum(W, axis=1))
    D_sparse = csr_matrix(D)

    # Construct the Laplacian matrix L
    L = D - W
    L_sparse = csr_matrix(L)

    # Convert the weighted adjacency matrix W to sparse format
    W_sparse = csr_matrix(W)

    return L_sparse, D_sparse, W_sparse
