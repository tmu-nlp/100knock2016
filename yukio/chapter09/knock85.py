from knock84 import make_matrix
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import PCA
import numpy as np
import pickle

def dimension_compression():
    X_t_c = make_matrix()
    token_list = []
    contexts_list = []
    for token, contexts in sorted(X_t_c.items()):
        token_list.append(token)
        contexts_list.append(contexts)

    pca = PCA(n_components = 300)
    DictoVec = DictVectorizer(sparse = True)

    sparse = DictoVec.fit_transform(contexts_list)

    print(sparse.shape)

    vec_list = pca.fit_transform(sparse.todense())
    
    word_vec = {}
    for token, vec in zip(token_list, vec_list):
        word_vec[token] = vec

    return word_vec

if __name__ == "__main__":
    word_vec = dimension_compression()
    with open("word_vec_85.pickle", "wb") as f:
        pickle.dump(word_vec, f)
