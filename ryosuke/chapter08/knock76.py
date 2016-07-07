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

for pre, t, (prob_n, prob_p) in zip(pred, y, pred_proba):
    prob = prob_n if pre == -1 else prob_p
    print('{}\t{}\t{}'.format(t, pre, prob))
