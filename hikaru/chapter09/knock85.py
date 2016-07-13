from scipy import sparse, io
import numpy as np
from sklearn import decomposition
import pickle

X = io.loadmat("matrix_X")["X"]
#X = X.todense()
#pca = decomposition.PCA(n_components = 300)
pca = decomposition.TruncatedSVD(n_components = 300)
pca.fit(X)
transformed = pca.transform(X)

print (type(transformed))
print (transformed.shape)
print (transformed)

with open('pca.pickle', mode='wb') as f:
    pickle.dump(transformed, f)
#with open('pca.pickle', mode='rb') as f:
    #pickle.load(f)
