import numpy as np
from sklearn.cluster import KMeans
import json
import plotly.plotly as py
import pandas as pd
import plotly.graph_objs as go


def json_to_array(json_file: dict) -> np.array:
    final_array = list()

    for country in json_file:
        temp_list = list()

        for atribute in json_file[country]:
            temp_list.append(json_file[country][atribute])

        final_array.append(temp_list)

    return np.array(final_array)


def execute_kmeans(n_clusters: int, data: np.array, labels: np.array):
    k_means = KMeans(n_clusters=n_clusters)

    k_means.fit(data)

    for i in range(n_clusters):
        print("Cluster {}".format(i))
        print(labels[k_means.labels_ == i])
        print()


if __name__ == '__main__':
    data_path = "datasets/onu2002.json"
    file = json.load(open(data_path))

    data = json_to_array(file)

    labels = np.array([country for country in file])

    execute_kmeans(4, data, labels)
