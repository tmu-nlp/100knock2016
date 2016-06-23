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
    count = 0
    total = 0
    for p, y in zip(pred, y_train):
        print(p, y)
        if int(p) == y:
            count += 1
        total += 1
    print(count/total)


if __name__ == '__main__':
    predict_function()
