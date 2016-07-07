from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from sklearn.cross_validation import cross_val_predict
from sklearn import metrics
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

pred = cross_val_predict(clf, x, y, cv=5, n_jobs=5)

acc = metrics.accuracy_score(y, pred)
pre = metrics.precision_score(y, pred)
rec = metrics.recall_score(y, pred)
f1 = metrics.f1_score(y, pred)
print('正解率:{:.3f}, 適合率:{:.3f}, 再現率:{:.3f}, F1:{:.3f}'.format(acc, pre, rec, f1))

