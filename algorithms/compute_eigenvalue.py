import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt

def compute_eigenvalues(L, k, title):
        
    # Compute eigenvalues using Arnoldi method 
    vals_arnoldi, vecs_arnoldi = spla.eigsh(L, k=k, which='SM', v0=None, maxiter=1000, tol=1e-6)

    # Compute eigenvalues using shift-invert method
    # sigma = 0.1  # choose a shift parameter
    # vals_shift, vecs_shift = spla.eigsh(L, k=k, sigma=sigma)

    # Plot the eigenvalues to visualize any gaps
    fig = plt.figure(figsize=(6, 4))
    plt.plot(range(1, k+1), vals_arnoldi, 'o-')
    plt.xlabel('Eigenvalue index')
    plt.ylabel('Eigenvalue')
    plt.title(f"{title} - Arnoldi")
    plt.show()

  # Compute the gaps between consecutive eigenvalues
    gaps = np.diff(vals_arnoldi)
    # Choose the number of clusters as the index of the largest gap
    num_clusters = np.argmax(gaps) + 1

    print(f'Number of clusters for {title} using Arnoldi algorithm:', num_clusters)

    return vals_arnoldi
