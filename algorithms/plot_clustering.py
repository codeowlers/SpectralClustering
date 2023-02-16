import matplotlib.pyplot as plt

def plot_clustering(type, num_clusters, title = ''):
    # Plot the clusters of points X with different colors
    colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
    for i in range(num_clusters):
        plt.scatter(type[i][:, 0], type[i][:, 1], c=colors[i % len(colors)], label='Cluster {}'.format(i+1))
    plt.legend()
    plt.title(title)
    plt.show()