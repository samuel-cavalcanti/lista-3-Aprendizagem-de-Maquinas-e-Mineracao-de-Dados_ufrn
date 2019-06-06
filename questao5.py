import numpy as np
from minisom import MiniSom


def generate_dataset() -> np.array:
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


if __name__ == '__main__':
    data = generate_dataset()

    som = MiniSom(10, 10, 8)

    som.train_random(data, 1000, verbose=True)

    weights = som.get_weights()

    weights = np.reshape(weights, (100, 8))

    print(weights.shape)

    np.savetxt("som_output.csv", weights, delimiter=",", header="x,x,x,x,x,x,x,x")
