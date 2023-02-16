from scipy.sparse.csgraph import connected_components


def compute_num_components(L):
    # Compute the number of connected components of the graph
    num_components, component_labels = connected_components(L)

    return num_components
