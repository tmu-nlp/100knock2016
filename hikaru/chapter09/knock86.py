import pickle
import numpy as np

with open('pca.pickle', mode='rb') as f:
    X = pickle.load(f)

print (X[7645])