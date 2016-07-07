from sklearn import cross_validation
from sklearn.cross_validation import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from knock75 import get_feature
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn.metrics import f1_score

if __name__ == "__main__":
    features_matrix = list()
    polarity_list = list()
    vec = DictVectorizer()
    for line in open("sentiment.txt", "r"):
        phi, polarity = get_feature(line)
        features_matrix.append(phi)
        polarity_list.append(polarity)
    X = vec.fit_transform(features_matrix)
    clf = LogisticRegression()
    predicted = cross_validation.cross_val_predict(clf, X, polarity_list, cv=5)
    print ('accuracy:{}'.format(metrics.accuracy_score(polarity_list, predicted)))
    print ('precision:{}'.format(metrics.precision_score(polarity_list, predicted)))
    print ('recall:{}'.format(metrics.recall_score(polarity_list, predicted)))
    print ('f:{}'.format(metrics.f1_score(polarity_list, predicted)))
