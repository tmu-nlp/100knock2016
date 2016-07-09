from knock72 import create_features, create_feature_vector
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
import numpy as np
from nltk import stem
from collections import defaultdict
from knock71 import getstopword

stoplist = getstopword()
stemmer = stem.PorterStemmer()

def get_feature(line):
    phi = defaultdict(int)
    words = line.strip("\n").split()
    for word in words[1:]:
        word = stemmer.stem(word)
        if word in stoplist:
            pass
        else:
            phi[word] += 1
    return phi, int(words[0])

if __name__ == "__main__":
    features_matrix = list()
    polarity_list = list()
    vec = DictVectorizer()
    #print (vec.fit_transform(phi).toarray())
    #print ((vec.fit_transform(phi)).todense())
    for line in open("sentiment.txt", "r"):
        phi, polarity = get_feature(line)
        features_matrix.append(phi)
        polarity_list.append(polarity)
    X = vec.fit_transform(features_matrix)
    #print(vec.inverse_transform(X[0]))
    #print(vec.get_feature_names()[15895])
    clf = LogisticRegression()
    clf.fit(X, polarity_list)
    joblib.dump(clf, 'knock75.model')
    #print (X.toarray())
    #print (len(clf.coef_[0])) #[[ 0.15670107  0.07262265 -0.49432087 ..., -0.11496645 -0.15299151 ]] 素性の数
    coef_dict = dict()
    for key, value in zip(vec.get_feature_names(), clf.coef_[0]):
        coef_dict[key] = value
    for key, value in sorted(coef_dict.items(), key=lambda x: -x[1])[:10]:
        print ('{} ----- {}'.format(key, value))
