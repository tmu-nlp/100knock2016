from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from sklearn.cross_validation import cross_val_predict
from sklearn import metrics
from knock72 import get_feature

import matplotlib.pyplot as plt

class proba_logres(LogisticRegression):
    def predict(self, X):
        return LogisticRegression.predict_proba(self, X)


clf = proba_logres()
dic2vec = DictVectorizer()
features = list()
y = list()
for line in open('sentiment.txt'):
    spl = line.rstrip('\n').split()
    label, sent = spl[0], ' '.join(spl[1:])
    features.append(get_feature(sent))
    y.append(int(label))
x = dic2vec.fit_transform(features)

probas = cross_val_predict(clf, x, y, cv=5, n_jobs=5)
precision, recall, thresholds = metrics.precision_recall_curve(y, probas[:, 1])
area = metrics.auc(recall, precision)

plt.plot(recall, precision, label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall example: AUC=%0.2f' % area)
plt.legend(loc="lower left")
plt.show()
