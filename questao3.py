from scipy.cluster.hierarchy import dendrogram, linkage, cut_tree
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


def fancy_dendrogram(*args, **kwargs):
    max_d = kwargs.pop('max_d', None)
    if max_d and 'color_threshold' not in kwargs:
        kwargs['color_threshold'] = max_d
    annotate_above = kwargs.pop('annotate_above', 0)

    ddata = dendrogram(*args, **kwargs)

    if not kwargs.get('no_plot', False):
        pyplot.title('Hierarchical Clustering Dendrogram (truncated)')
        pyplot.xlabel('sample index or (cluster size)')
        pyplot.ylabel('distance')
        for i, d, c in zip(ddata['icoord'], ddata['dcoord'], ddata['color_list']):
            x = 0.5 * sum(i[1:3])
            y = d[1]
            if y > annotate_above:
                pyplot.plot(x, y, 'o', c=c)
                pyplot.annotate("%.3g" % y, (x, y), xytext=(0, -5),
                                textcoords='offset points',
                                va='top', ha='center')
        if max_d:
            pyplot.axhline(y=max_d, c='k')
    return ddata


if __name__ == '__main__':
    data_path = "datasets/onu2002.json"
    file = json.load(open(data_path))

    data = json_to_array(file)

    linked = linkage(data, method="ward", metric="euclidean", optimal_ordering=True)

    pyplot.figure("dendrogram")

    labels = np.array([country for country in file])

    fancy_dendrogram(linked, labels=labels, max_d=2)

    pyplot.show()
