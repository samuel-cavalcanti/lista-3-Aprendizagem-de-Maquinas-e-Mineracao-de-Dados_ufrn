import numpy as np
import matplotlib.pyplot as pyplot

if __name__ == '__main__':
    file_name = "datasets/soilDataset.csv"
    data = np.loadtxt(file_name, delimiter=",") / 100

    for i, col in enumerate(data.T):
        max_x = np.max(col)
        min_x = np.min(col)
        mean = np.mean(col)
        std = np.std(col)
        median = np.median(col)
        print("X_{}".format(i + 1))
        print("max {}".format(max_x))
        print("min {}".format(min_x))
        print("mean {}".format(mean))
        print("standard deviation {}".format(std))
        print("median {}".format(median))

    cov_matrix = np.cov(data)

    eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)

    eigenvectors = -np.sort(-eigenvectors)

    eigenvalues = -np.sort(-eigenvalues)
