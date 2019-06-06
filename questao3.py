from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import json
from matplotlib import pyplot


def json_to_array(json_file: dict) -> np.array:
    final_array = list()

    for country in json_file:
        temp_list = list()

        for atribute in json_file[country]:
            temp_list.append(json_file[country][atribute])

        final_array.append(temp_list)

    return np.array(final_array)


if __name__ == '__main__':
    data_path = "datasets/onu2002.json"
    file = json.load(open(data_path))

    data = json_to_array(file)

    linked = linkage(data, method="ward", metric="euclidean")

    pyplot.figure("dendrogram")

    labels = np.array([country for country in file])

    dendrogram(linked, orientation="top", labels=labels, distance_sort="descending")

    pyplot.show()
