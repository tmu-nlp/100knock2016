from scipy import io, sparse
from scipy.sparse.linalg import svds
import numpy as np
import pickle


def dimension_reduction():
    X = io.loadmat('matrix')['PPMI']
    word_list = list()
    for line in open('word_list.txt', 'r'):
        key, value = line.strip('\n').split('\t')
        word_list.append(key)

    X_svd = svds(X, 300)
    X_pca = np.dot(X_svd[0], np.diag(X_svd[1]))
    word_matrix = dict()
    for word, vector in zip(word_list, X_pca):
        word_matrix[word] = vector

    return word_matrix

if __name__ == '__main__':
    word_matrix = dimension_reduction()
    with open('knock85_result.dump', 'wb') as f:
        pickle.dump(word_matrix, f)
