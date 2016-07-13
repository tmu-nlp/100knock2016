import pickle
import numpy as np
from collections import defaultdict
import math

with open('pca.pickle', mode='rb') as f1:
    X = pickle.load(f1)
with open('t_index.pickle', mode='rb') as f2:
    t_index = pickle.load(f2)

def cosine_similarity(v1, v2):
    return sum([a*b for a, b in zip(v1, v2)])/(sum(map(lambda x: x*x, v1))**0.5 * sum(map(lambda x: x*x, v2))**0.5)
def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

X_dict = dict()
for key, value in sorted(t_index.items(), key=lambda x: x[1])[:30000]:
    X_dict[key] = X[value]
V = X_dict['Spain'] - X_dict['Madrid'] + X_dict['Athens']
print (type(X_dict["Spain"]))
cos_dict = dict()
for key, value in sorted(t_index.items(), key=lambda x: x[1])[:30000]:
    if math.isnan(cos_sim(V, X_dict[key])):
        pass
    else:
        cos_dict[key] = cos_sim(V, X_dict[key])
    #print ('{}   {}'.format(key, cos_dict[key]))

for key, value in sorted(cos_dict.items(), key=lambda x: -x[1])[:11]:
    print ('{}----------{}'.format(key, value))
print (cos_dict['Greece'])