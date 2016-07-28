import numpy as np
import pickle
from knock84 import word_id
import scipy.spatial.distance as dis

with open("truncated_X.dump","rb") as f:
    X = pickle.load(f)
X = X.tocsr()
score_dict = {}
sum_vec = X[word_id["Spain"]] - X[word_id["Madrid"] + X[word_id["Athens"]]]

for key, value in word_id.items():
    cosine = dis.cosine(sum_vec,X[value])
    score_dict[key] = cosine
c = 0
for key,value in sorted(score_dict.items(), key=lambda x: -x):
    if c > 10:
        break
    print(key)
    c += 1
