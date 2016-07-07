from knock72 import get_feature
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from collections import Counter


def log_regression():
    x_list = []
    logreg = LogisticRegression()
    y_train, x_train = get_feature()
    for line in x_train:
        x_list.append(dict(Counter(line)))
    word_vec = DictVectorizer()
    X = word_vec.fit_transform(x_list)
    logreg.fit(X, y_train)
    joblib.dump(logreg, 'logreg.pkl')
    joblib.dump(word_vec,"word_vec.pkl")


if __name__ == '__main__':
    log_regression()
