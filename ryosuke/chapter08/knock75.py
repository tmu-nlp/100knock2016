from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from knock72 import get_feature

clf = joblib.load('knock73.model')
dic2vec = DictVectorizer()

features = list()
for line in open('sentiment.txt'):
    spl = line.rstrip('\n').split()
    label, sent = spl[0], ' '.join(spl[1:])
    features.append(get_feature(sent))
x = dic2vec.fit_transform(features)
features = dic2vec.get_feature_names()

# top 10
print('top 10')
for i in clf.coef_[0].argsort()[-10:][::-1]:
    print(features[i], clf.coef_[0][i])

# top -10
print()
print('top -10')
for i in clf.coef_[0].argsort()[:10]:
    print(features[i], clf.coef_[0][i])
