import pickle
import numpy as np
import scipy.spatial.distance
from collections import defaultdict

with open('knock85_result.dump', 'rb') as fp:
  word_vector = pickle.load(fp)
  similarity = defaultdict(lambda: 0.0)

  w1 = word_vector['Spain']
  w2 = word_vector['Madrid']
  w3 = word_vector['Athens']
  w4 = w1 - w2 + w3

  for word in word_vector.keys():
    if word != 'England':
      w5 = word_vector[word]
      similarity[word] = 1 - scipy.spatial.distance.cosine(w4, w5)

  count = 0
  for word, sim in sorted(similarity.items(), key=lambda x:x[1], reverse=True):
    print("{}\t{}".format(word, sim))
    count += 1
    if count == 10:
      break


