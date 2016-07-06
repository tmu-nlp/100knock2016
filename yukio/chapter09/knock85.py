from knock84 import make_matrix
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.decomposition import PCA
import numpy as np

def dimension_compression():
    X_t_c = make_matrix()
    token_list = []
    contexts_list = []
    for token, contexts in sorted(X_t_c.items()):
        token_list.append(token)
        contexts_list.append(contexts)

    pca = PCA(n_components = 300)
    DictoVec = DictVectorizer(sparse = False)

    vec_list = pca.fit_transform(DictoVec.fit_transform(contexts_list))
    
    word_vec = {}
    for token, vec in zip(token_list, vec_list):
        word_vec[token] = vec

    return word_vec

if __name__ == "__main__":
    word_vec = dimension_compression()
    f = open("word_vec_85.txt", "w")
    for key, value in sorted(word_vec.items()):
        print("vec({}) : {}".format(key, value))
        f.write("{}\t{}\n".format(key, value))
    f.close()
