from knock72 import getFeature
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer


if __name__ == '__main__':
    dic2vec = DictVectorizer()
    features = list()
    y = list()
    for line in open('sentiment.txt'):
        word_list = line[3:].strip('\n').strip().split()
        label = line[:2]
        features.append(getFeature(word_list))
        y.append(int(label))
    x = dic2vec.fit_transform(features)
    lr = LogisticRegression()
    lr.fit(x, y)
    joblib.dump(lr, 'lr.pkl')
