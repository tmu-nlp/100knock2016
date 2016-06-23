from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature


clf = LogisticRegression()
dic2vec = DictVectorizer()
features = list()
y = list()
for line in open('sentiment.txt'):
    spl = line.rstrip('\n').split()
    label, sent = spl[0], ' '.join(spl[1:])
    features.append(get_feature(sent))
    y.append(int(label))
x = dic2vec.fit_transform(features)
clf.fit(x, y)

joblib.dump(clf, 'knock73.model')
