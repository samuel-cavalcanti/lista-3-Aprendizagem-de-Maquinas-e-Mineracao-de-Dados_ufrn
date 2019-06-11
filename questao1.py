import numpy as np
import matplotlib.pyplot as pyplot


def plot_cov_matrix(matrix: np.array, title: str):
    pyplot.matshow(matrix, cmap=pyplot.cm.Blues)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            pyplot.text(i, j, str(round(matrix[i][j], 2)), va="center", ha="center", color="red")

    pyplot.title(title, fontsize=20)
    pyplot.colorbar()
    pyplot.show()


def plot_PCA(Y: np.array):
    title = "Matriz das Componentes principais"
    pyplot.figure(title, figsize=Y.shape)

    pyplot.pcolor(Y, cmap=pyplot.cm.Blues)
    for i in range(len(Y)):
        for j in range(len(Y[i])):
            pyplot.text(j + 0.35, i + 0.3, str(round(Y[i][j], 2)), color="red")

    pyplot.text(0.4, len(Y) + 0.3, "Y1")
    pyplot.text(1.4, len(Y) + 0.3, "Y2")
    pyplot.text(2.4, len(Y) + 0.3, "Y3")
    pyplot.text(3.4, len(Y) + 0.3, "Y4")

    pyplot.colorbar()
    pyplot.title(title, fontsize=10, y=1, x=0.49)
    pyplot.show()


def plot_eigenvectors(eigenvectors: np.array, eigenvalues: np.array):
    title = "Auto Vetores"
    pyplot.matshow(eigenvectors, cmap=pyplot.cm.Blues)

    for i in range(len(eigenvectors)):
        for j in range(len(eigenvectors[i])):
            pyplot.text(j, i, round(eigenvectors[i][j], 3), color="red", ha="center", va="center")

    pyplot.title(title, fontsize=20)

    pyplot.colorbar()

    pyplot.text(-1.3, 3.85, "Auto", fontsize=20)
    pyplot.text(-1.35, 4.05, "Valores: ", fontsize=20)
    for i, eigenvalue in enumerate(eigenvalues):
        pyplot.text(i, 4, np.round(eigenvalue, 2), ha="center", va="center")
        if i == 2:
            pyplot.text(i, 4.5, "X{}".format(i + 2), ha="center")
        elif i == 3:
            pyplot.text(i, 4.5, "X{}".format(i - 1), ha="center")
        else:
            pyplot.text(i, 4.5, "X{}".format(i + 1), ha="center")

    # pyplot.text(0, 4, " ({}, {}, {}, {})".format(round(eigenvalues[0], 2), round(eigenvalues[1], 2),
    #                                              round(eigenvalues[2], 2), round(eigenvalues[3], 2)))

    pyplot.show()


def descriptive_statistics(data: np.array):
    for i, col in enumerate(data.T):
        max_x = np.max(col)
        min_x = np.min(col)
        mean = np.mean(col)
        std = np.std(col)
        median = np.median(col)
        print("X_{}".format(i + 1))
        print("max: {}".format(max_x))
        print("min: {}".format(min_x))
        print("mean: {}".format(mean))
        print("standard deviation: {}".format(std))
        print("median: {}".format(median))


def a(data: np.array, plot=False) -> np.array:
    cov_matrix = np.cov(data, rowvar=False)

    if plot:
        plot_cov_matrix(cov_matrix, "Matriz de covariancia")

    return cov_matrix


def b(data: np.array, plot=False) -> (np.array, np.array):
    cov_matrix = a(data)

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
    eigenvalues = -np.sort(-eigenvalues)

    temp = np.copy(eigenvectors[:, 2])
    eigenvectors[:, 2] = eigenvectors[:, 3]
    eigenvectors[:, 3] = temp

    if plot:
        plot_eigenvectors(eigenvectors, eigenvalues)

    return eigenvectors, eigenvalues


def c(X: np.array, plot=False):
    eigenvectors, _ = b(X)

    e1 = eigenvectors[:, 0] / np.linalg.norm(eigenvectors[:, 0])

    e2 = eigenvectors[:, 1] / np.linalg.norm(eigenvectors[:, 1])

    # eu troquei o X3 pelo X4 na questão anterior

    e4 = eigenvectors[:, 2] / np.linalg.norm(eigenvectors[:, 2])

    e3 = eigenvectors[:, 3] / np.linalg.norm(eigenvectors[:, 3])

    E = np.vstack((e1, e2, e3, e4))

    Y = X.dot(E)

    if plot:
        plot_PCA(Y)


def d(data: np.array):
    _, eigenvalues = b(data)

    print(np.round(eigenvalues / np.sum(eigenvalues), 3))


if __name__ == '__main__':
    file_name = "datasets/soilDataset.csv"
    dataset = np.loadtxt(file_name, delimiter=",")
    descriptive_statistics(dataset)
    a(dataset)
    b(dataset)
    c(dataset)
    d(dataset)
