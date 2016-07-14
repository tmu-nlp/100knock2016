import pickle
import numpy as np
import scipy.spatial.distance
from collections import defaultdict

with open('knock85_result.dump', 'rb') as fp:
  word_vector = pickle.load(fp)
  similarity = defaultdict()
  w1 = word_vector['England']
  for word in word_vector.keys():
    if word != 'England':
      w2 = word_vector[word]
      similarity[word] = 1 - scipy.spatial.distance.cosine(w1, w2) 

  count = 0
  for word, sim in sorted(similarity.items(), key=lambda x:x[1], reverse=True)[:10]:
    print("{}\t{}".format(word, sim))
