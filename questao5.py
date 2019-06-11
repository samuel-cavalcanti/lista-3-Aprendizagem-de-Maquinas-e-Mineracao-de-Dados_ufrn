import numpy as np
from minisom import MiniSom
from scipy.spatial import distance
from matplotlib import pyplot
from matplotlib.gridspec import GridSpec


def make_dataset() -> np.array:
    m1 = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    m2 = np.array([4, 0, 0, 0, 0, 0, 0, 0])

    m3 = np.array([0, 0, 0, 4, 0, 0, 0, 0])

    m4 = np.array([0, 0, 0, 0, 0, 0, 0, 4])

    sigma = np.eye(8)

    n1 = np.random.multivariate_normal(m1, sigma, 1000)

    n2 = np.random.multivariate_normal(m2, sigma, 1000)

    n3 = np.random.multivariate_normal(m3, sigma, 1000)

    n4 = np.random.multivariate_normal(m4, sigma, 1000)

    return np.concatenate((n1, n2, n3, n4))


def make_labels_map() -> np.array:
    labels_array = list()
    labels = ["n1 (0, 0, 0, 0, 0, 0, 0, 0)", "n2 (4, 0, 0, 0, 0, 0, 0, 0)",
              "n3 (0, 0, 0, 4, 0, 0, 0, 0)", "n4 (0, 0, 0, 0, 0, 0, 0, 4)"]

    for label in labels:
        temp_array = [label for i in range(1000)]
        labels_array += temp_array
    return np.array(labels_array)


def train_som(data: np.array, m_din: int, n_din: int, features_size: int) -> MiniSom:
    som = MiniSom(m_din, n_din, features_size)

    som.train_random(data, 1000, verbose=True)

    return som


def u_matrix(som: MiniSom, data: np.array, labels: np.array):
    distance_map = som.distance_map()
    markers = ["o", "s", "D", "v"]

    name_fig1 = "U matrix"
    pyplot.figure(name_fig1, figsize=distance_map.shape)

    pyplot.pcolor(distance_map, cmap="bone_r")

    for i, marker in enumerate(markers):
        winners = np.array(list(som.win_map(data[1000 * i:1000 * (i + 1)]).keys()))

        pyplot.plot(winners[:, 0] + 0.5, winners[:, 1] + 0.5, marker, markersize=12, markeredgewidth=2,
                    label=labels[i])

    pyplot.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,
                  ncol=2, mode="expand", borderaxespad=0.)

    pyplot.title(name_fig1)


def activations_frequencies(som: MiniSom, data: np.array):
    distance_map = som.distance_map()

    name_fig2 = "Activations frequencies"

    pyplot.figure(name_fig2, figsize=distance_map.shape)
    pyplot.title(name_fig2)

    frequencies = np.zeros(distance_map.shape)

    for position, values in som.win_map(data).items():
        frequencies[position[0], position[1]] = len(values)

    pyplot.pcolor(frequencies, cmap='Blues')
    pyplot.colorbar()


def class_pies(som: MiniSom, data: np.array, labels: np.array):
    distance_map = som.distance_map()
    label_names = np.unique(labels)
    name_fig3 = "Class pies"

    the_grid = GridSpec(distance_map.shape[0], distance_map.shape[0])
    labels_map = som.labels_map(data, make_labels_map())

    pyplot.figure(name_fig3, figsize=distance_map.shape)

    for position in labels_map.keys():
        label_fracs = [labels_map[position][l] for l in label_names]
        pyplot.subplot(the_grid[9 - position[1], position[0]])
        patches, texts = pyplot.pie(label_fracs)

    pyplot.subplot(the_grid[0, 0])

    pyplot.legend(labels, ncol=2, bbox_to_anchor=(5.5, -11.6, 2., .102), loc="center")

    pyplot.title(name_fig3, x=5.5, y=1.5, fontsize=30)


def visualize_som(som: MiniSom, data: np.array):
    labels = ["n1 (0, 0, 0, 0, 0, 0, 0, 0)", "n2 (4, 0, 0, 0, 0, 0, 0, 0)",
              "n3 (0, 0, 0, 4, 0, 0, 0, 0)", "n4 (0, 0, 0, 0, 0, 0, 0, 4)"]

    u_matrix(som, data, labels)
    activations_frequencies(som, data)
    class_pies(som, data, labels)
    pyplot.show()


if __name__ == '__main__':
    data = make_dataset()

    dim_som = 10

    som = train_som(data, dim_som, dim_som, data[0].size)

    visualize_som(som, data)
