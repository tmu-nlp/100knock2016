from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature
from collections import Counter


def predict_function():
    x_list = []
    predict_doc = joblib.load('logreg.pkl')
    y_train, x_train = get_feature()
    for line in x_train:
        x_list.append(dict(Counter(line)))
    X = DictVectorizer().fit_transform(x_list)
    pred = predict_doc.predict(X)
    prob = predict_doc.predict_proba(X)
    return pred, y_train, prob


if __name__ == '__main__':
    pred, y_train, prob = predict_function()
    for a, y, p in zip(pred, y_train, prob):
        print("{}\t{}\t{}".format(a, y, max(*p)))
