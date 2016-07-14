import pickle
import numpy as np
import scipy.spatial.distance

with open('knock85_result.dump', 'rb') as fp:
  word_vector = pickle.load(fp)
  w1 = word_vector['United_States']
  w2 = word_vector['U.S']
  print(1- scipy.spatial.distance.cosine(w1, w2))


