from knock83 import pair_counting
from collections import defaultdict
from scipy.sparse import lil_matrix
import math


def PPMI_matrix():
    ftc, ft, fc, N = pair_counting()
    print('function "pair counting" finished.')
    print('ftc: {}, ft: {}, fc: {}'.format(len(ftc), len(ft), len(fc)))
    X = lil_matrix((len(ft), len(ft)))
    word_id = defaultdict(lambda: len(word_id))
    [word_id[key] for key in sorted(ft.keys())]
    for key, value in sorted(ftc.items()):
        if value < 10:
            continue
        word_t, word_c = key.split('\t')
        pmi = math.log((N * value) / (ft[word_t] * fc[word_c]))
        if pmi > 0 and word_c in word_id:
            X[word_id[word_t], word_id[word_c]] = pmi
    return X, word_id

if __name__ == '__main__':
    X = PPMI_matrix()
