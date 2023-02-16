import matplotlib.pyplot as plt
def plot_datasets(X1, title1, X2, title2):
 
    # Plot the first dataset
    plt.subplot(1, 2, 1)
    plt.scatter(X1[:, 0], X1[:, 1], c='blue')
    plt.title(title1)

    # Plot the second dataset
    plt.subplot(1, 2, 2)
    plt.scatter(X2[:, 0], X2[:, 1], c='blue')
    plt.title(title2)

    plt.show()
