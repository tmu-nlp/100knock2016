from knock73 import feature_making, feature_vector
from collections import defaultdict
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
import numpy as np
import sys

def unknown_remove(query, feature_dict):
    for word in query:
        if word not in feature_dict:
            query.remove(word)
    return query


def fit_feature(query, feature_dict):
    matrix = []
    query = unknown_remove(feature_making(query), feature_dict)
    matrix.append(feature_vector(query))
    matrix.append(feature_dict)
    dicvec = DictVectorizer()
    feature = dicvec.fit_transform(matrix)[0]
    return feature


if __name__ == '__main__':
    feature_dict = dict()
    for line in open('knock72_result.txt'):
        word, value = line.strip('\n').split('\t')
        feature_dict[word] = int(value)

    LR = joblib.load('LR.pkl')
    query = sys.argv[1:]
    
    feature = fit_feature(query, feature_dict)
    polarity = '+1' if LR.predict(feature)[0] == 1 else '-1'
    probability = LR.predict_proba(feature)[0]

    print('{}: {}'.format(polarity, max(probability[0], probability[1])))
