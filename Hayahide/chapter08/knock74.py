from knock73 import feature_vector, feature_making
from sklearn.externals import joblib
import numpy as np
import sys

feature_list = list()
for line in open('knock72_result.txt'):
    word = line.strip('\n')
    feature_list.append(word)

LR = joblib.load('LR.pkl')

query = sys.argv[1:]
vector = []
query = feature_making(query)
vector.append(feature_vector(feature_list, query))

polarity = LR.predict(vector)[0]
print('Positive' if polarity > 0 else 'Negative')
probability = LR.predict_proba(vector)[0]
print(probability[0] if probability[0] > probability[1] else probability[1])
