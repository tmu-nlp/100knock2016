from knock83 import pair_counting
from collections import defaultdict
from scipy.sparse import lil_matrix
from scipy import io
import math


def PPMI_matrix():
    ftc, ft, fc, N = pair_counting()
    print('pair_counting finished.')
    X = lil_matrix((30000, 30000))
    word_id = defaultdict(lambda: len(word_id))
    [word_id[key] for key, value in sorted(ft.items(), key=lambda x:x[1], reverse=True)[:30000]]
    for key, value in sorted(ftc.items(), key=lambda x:x[1], reverse=True):
        if value < 10:
            continue
        word_t, word_c = key.split('\t')
        if word_t in word_id and word_c in word_id:
            pmi = math.log((N * value) / (ft[word_t] * fc[word_c]))
            if pmi > 0:
                X[word_id[word_t], word_id[word_c]] = pmi

    w_file = open('word_list.txt', 'w')
    for key, value in sorted(word_id.items(), key=lambda x:x[1], reverse=True):
        w_file.write(key + '\t' + str(value) + '\n')
    w_file.close()

    return X

if __name__ == '__main__':
    io.savemat("matrix", {"PPMI": PPMI_matrix()})
