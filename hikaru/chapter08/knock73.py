from knock72 import create_features, create_feature_vector
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
import numpy as np

if __name__ == "__main__":
    phi = create_features("sentiment.txt")
    features_matrix = list()
    polarity_list = list()
    for line in open("sentiment.txt", "r"):
        feature_vector, polarity = create_feature_vector(line, phi)
        features_matrix.append(feature_vector)
        polarity_list.append(polarity)
    #print (np.array(features_matrix).shape)
    #print (np.array(polarity_list).shape)
    clf = LogisticRegression(C = 1000) #ここ1000にしたら確率変わらなくなった デフォルトは1.0
    clf.fit(features_matrix, polarity_list)
    joblib.dump(clf, 'clf.pkl')
