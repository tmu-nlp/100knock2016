from sklearn.externals import joblib
from knock72 import create_feature_vector, create_features
import sys

if __name__ == "__main__":
    clf = joblib.load('clf.pkl')
    phi = create_features("sentiment.txt")
    feature_vector, polarity = create_feature_vector(sys.argv[1], phi)
    matrix = list() #1次元配列だと怒られる
    matrix.append(feature_vector)
    print (clf.predict(matrix))
    print (clf.predict_proba(matrix))