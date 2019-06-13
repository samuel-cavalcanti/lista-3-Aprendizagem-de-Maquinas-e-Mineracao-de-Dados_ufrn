import numpy as np
from scipy import signal
import scipy.io.wavfile

import sklearn.decomposition

# https://github.com/subokita/Sandbox/blob/master/blind_source.py
if __name__ == '__main__':
    rate, source = scipy.io.wavfile.read("TokyoDrift.wav")

    source_1 = source[:, 0]

    source_2 = source[:, 1]

    data = np.c_[source_1, source_2]

    data = data / 2.0 ** 15

    fast_ica = sklearn.decomposition.FastICA(n_components=2)

    separated = fast_ica.fit_transform(data)

    assert np.allclose(data, separated.dot(fast_ica.mixing_.T) + fast_ica.mean_)

    max_source = 1.0
    min_source = -1

    max_result = np.max(separated.flatten())
    min_result = np.min(separated.flatten())



    separated = map(lambda x: (2.0 * (x - min_result)) / (max_result - min_result) + -1.0, separated.flatten())


    separated

    separated = np.reshape(separated, (np.shape(separated)[0] / 2, 2))

    # Store the separated audio, listen to them later
    scipy.io.wavfile.write('separated_1.wav', rate, separated[:, 0])
    scipy.io.wavfile.write('separated_2.wav', rate, separated[:, 1])