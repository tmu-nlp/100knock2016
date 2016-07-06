from knock72 import getFeature
from knock77 import get_eval
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
# from sklearn import cross_validation
import numpy as np
from sklearn.cross_validation import KFold

'''
def get_score(lr, train_features, train_labels):
    #X_train, X_test, y_train, y_test = cross_validation.train_test_split(train_features, train_labels, test_size = 0.2, random_state=0)
    #lr.fit(X_train, y_train)
    accuracy = cross_validation.cross_val_score(lr, train_features, train_labels, cv=5, scoring='accuracy')
    precision = cross_validation.cross_val_score(lr, train_features, train_labels, cv=5, scoring='precision')
    recall = cross_validation.cross_val_score(lr, train_features, train_labels, cv=5, scoring='recall')
    f1 = cross_validation.cross_val_score(lr, train_features, train_labels, cv=5, scoring='f1')
    print('accuracy:{0:.3f}'.format(accuracy.mean()))
    print('precision:{0:.3f}'.format(precision.mean()))
    print('accuracy:{0:.3f}'.format(recall.mean()))
    print('f1:{0:.3f}'.format(f1.mean()))
'''

def eval_cv5(model, x, y):
    kf = KFold(len(y), n_folds=5)
    acc = np.array([])
    pre = np.array([])
    rec = np.array([])
    f1 = np.array([])
    for train_index, test_index in kf:
        x_train, x_test = x[train_index], x[test_index]
        y_train, y_test = y[train_index], y[test_index]
        model.fit(x_train, y_train)
        prediction = model.predict(x_test)
        evaluation = get_eval(prediction, y_test)
        acc = np.append(acc, np.array(evaluation[0]))
        pre = np.append(pre, np.array(evaluation[1]))
        rec = np.append(rec, np.array(evaluation[2]))
        f1 = np.append(f1, np.array(evaluation[3]))

    return acc.mean(), pre.mean(), rec.mean(), f1.mean()

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
    y = np.array(y)
    lr = LogisticRegression()
    acc, pre, rec, f1 = eval_cv5(lr, x, y)
    # get_score(lr, x, y)
    print('accuracy: {0:.3f}'.format(acc))
    print('precision: {0:.3f}'.format(pre))
    print('recall: {0:.3f}'.format(rec))
    print('F1: {0:.3f}'.format(f1))
