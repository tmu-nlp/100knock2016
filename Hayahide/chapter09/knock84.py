from knock83 import pair_counting
from collections import defaultdict
import math


def PPMI_matrix():
    ftc, ft, fc, N = pair_counting()
    X = defaultdict(lambda: defaultdict(float))
    for key, value in ftc.items():
        if value < 10:
            continue
        word_t, word_c = key.split('\t')
        if word_t in ft and word_c in fc:
            pmi = math.log((N * value) / (ft[word_t] * fc[word_c]), 2)
            if pmi > 0:
                X[word_t][word_c] = pmi
    return X

if __name__ == '__main__':
    X = PPMI_matrix()
