import numpy as np
import pickle
from knock84 import word_id
import scipy.spatial.distance as dis

with open("truncated_X.dump","rb") as f:
    X = pickle.load(f)
score_dict = {}
for key, value in word_id.items():
    cosine = dis.cosine(X[word_id["England"]],X[value])
    score_dict[key] = cosine
c = 0
for key,value in sorted(score_dict.items(), key=lambda x: -x):
    if c > 10:
        break
    print(key)
    c += 1
