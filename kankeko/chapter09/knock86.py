import numpy as np
import pickle
from knock84 import word_id


with open("truncated_X.dump","rb") as f:
    X = pickle.load(f)


print(X[word_id["United_States"]],X[word_id["U.S"]])


