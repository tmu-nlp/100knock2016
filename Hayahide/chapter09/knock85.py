from knock84 import PPMI_matrix
from sklearn.feature_extraction import DictVectorizer
from scipy.sparse.linalg import svds
import numpy as np
import pickle


def dimension_reduction():
    X = PPMI_matrix()
    word_list = list()
    vecdict_list = list()
    for word, vector in sorted(X.items()):
        word_list.append(word)
        vecdict_list.append(dict(vector))
    Dic2Vec = DictVectorizer(sparse=True)
    vector_list = Dic2Vec.fit_transform(vecdict_list)

    X_svd = svds(vector_list, 300)
    X_pca = np.dot(X_svd[0], np.diag(X_svd[1]))
    word_matrix = dict()
    for word, vector in zip(word_list, X_pca):
        word_matrix[word] = vector

    return word_matrix

if __name__ == '__main__':
    word_matrix = dimension_reduction()
    with open('knock85_result.dump', 'wb') as f:
        pickle.dump(word_matrix, f)
