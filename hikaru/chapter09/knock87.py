import pickle
import numpy as np

with open('pca.pickle', mode='rb') as f:
    X = pickle.load(f)

def cosine_similarity(v1, v2):
    return sum([a*b for a, b in zip(v1, v2)])/(sum(map(lambda x: x*x, v1))**0.5 * sum(map(lambda x: x*x, v2))**0.5)
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

print (cosine_similarity(X[7645], X[182]))
print (cos_sim(X[7645], X[182]))