import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


def a(data: np.array, n_centroids: int):
    k_means = KMeans(n_clusters=n_centroids)

    k_means.fit(data)

    print(k_means.cluster_centers_)

    plot_k_means(k_means, data)


def b(data: np.array, n_centroids: int):
    init_pos = np.array(
        [
            [0, 0, 0],
            [1, 1, 1],
            [-1, 0, 2]
        ]
    )

    k_means = KMeans(n_clusters=n_centroids, init=init_pos)

    k_means.fit(data)

    plot_k_means(k_means, data)


def c(data: np.array, n_centroids: int):
    init_pos = np.array(
        [
            [-0.1, 0, 0.1],
            [0, -0.1, 0.1],
            [-0.1, -0.1, 0.1]
        ]
    )

    k_means = KMeans(n_clusters=n_centroids, init=init_pos)

    k_means.fit(data)

    plot_k_means(k_means, data)


def plot_k_means(k_means: KMeans, data: np.array):
    colors = ["blue", "orange", "green"]
    pyplot.figure("K-Means")

    ax = pyplot.axes(projection="3d")

    for i in range(len(k_means.cluster_centers_)):
        ax.scatter(data[k_means.labels_ == i, 0], data[k_means.labels_ == i, 1], data[k_means.labels_ == i, 2], "o",
                   label="class {}".format(i + 1))

    for i, centroid in enumerate(k_means.cluster_centers_):
        ax.scatter(centroid[0], centroid[1], centroid[2], "O",
                   s=100, color=colors[i])

    pyplot.show()


if __name__ == '__main__':
    dataset = np.loadtxt("datasets/table.csv", delimiter=",")

    a(dataset, 3)

    b(dataset, 3)

    c(dataset, 3)
