import numpy as np
import pickle
from scipy import io
from  sklearn.decomposition import TruncatedSVD
from  sklearn.decomposition import PCA


def compress_the_dimension():
    X = io.loadmat("X_matrix")['PPMI']
    a = PCA(300)
    a.fit(X)
    #decomp = TruncatedSVD(n_components=300, n_iter=7)
    #decomp.fit(X)
    truncated_X = decomp.transform(X)

    return truncated_X

if __name__ =="__main__":
    truncated_X = compress_the_dimension()
    with open("truncated_X.dump","wb") as f:
        pickle.dump(truncated_X, f)
