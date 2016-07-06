from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature

clf = joblib.load('knock73.model')
dic2vec = DictVectorizer()
features = list()
y = list()
sents = list()
for line in open('sentiment.txt'):
    spl = line.rstrip('\n').split()
    label, sent = spl[0], ' '.join(spl[1:])
    sents.append(sent)
    features.append(get_feature(sent))
    y.append(int(label))
x = dic2vec.fit_transform(features)
pred = clf.predict(x)
pred_proba = clf.predict_proba(x)

for pre, proba, sent in zip(pred, pred_proba, sents):
    print(pre, proba, sent)
