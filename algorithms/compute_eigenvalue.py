import numpy as np
from scipy.sparse.linalg import eigsh
def compute_eigenvalues(L, k):
    # Compute the first k smallest eigenvalues and corresponding eigenvectors of the Laplacian matrix
    num_eigvals = min(k, L.shape[0]-1)
    eigvals, eigvecs = eigsh(L, k=num_eigvals, which='SM')

    # Sort the eigenvalues in ascending order
    sorted_eigvals = np.sort(eigvals)

    # Plot the sorted eigenvalues
    import matplotlib.pyplot as plt
    plt.plot(sorted_eigvals)
    plt.show()

    # Choose the number of clusters based on the number of small eigenvalues
    num_clusters = np.sum(sorted_eigvals < 1e-10)  # or adjust the threshold as needed
    print("Number of clusters: ", num_clusters) 

    return sorted_eigvals, eigvals
