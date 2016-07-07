from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature
from collections import Counter


def predict_function():
    x_list = []
    line_list = []
    line_dict = {}
    predict_doc = joblib.load('logreg.pkl')
    feature_doc = joblib.load("word_vec.pkl")
    y_train, x_train = get_feature()
    line = "bad bad good good"
    line_list = line.split()
    for line in x_train:
        for key in line:
            line_dict[key] = 0
    line_dict.update(dict(Counter(line_list)))
    for a in sorted(line_dict.items(), key = lambda x:x[1]):
        print(a)
    x_list.append(line_dict)
    print(x_list)
    exit()
    X = DictVectorizer().fit_transform(x_list)
    pred = predict_doc.predict(X)
    prob = predict_doc.predict_proba(X)
    for pred, prob in zip(pred,prob):
        print(pred, prob)


if __name__ == '__main__':
    predict_function()
