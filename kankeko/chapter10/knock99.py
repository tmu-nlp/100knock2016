from sklearn import cluster
import numpy as np
from knock96 import countries_dict
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE


features = []
for key, value in countries_dict.items():
    features.append(value)

tsne_result = TSNE().fit_transform(features)
plt.plot(tsne_result[:,0], tsne_result[:,1], ".")
plt.show()
