from knock72 import getFeature
from knock77 import get_eval 
from knock78 import eval_cv5
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from sklearn.feature_extraction import DictVectorizer
from sklearn import cross_validation
import matplotlib.pyplot as plt
import numpy as np
from sklearn.cross_validation import KFold

def plot_p_r(train_features, train_labels):
    precision_l = list()
    recall_l = list()
    t_list = np.arange(0, 1, 0.1)
    for thd in t_list:
        lr = LogisticRegression()
        kf = KFold(len(train_labels), n_folds=5)
        for train_index, test_index in kf:
            x_train, x_test = x[train_index], x[test_index]
            y_train, y_test = y[train_index], y[test_index]
            lr.fit(x_train, y_train)
            prediction = lr.predict_proba(x_test)
            y_predict = list()
            precision = np.array([])
            recall = np.array([])

            for prob in prediction:
                if prob[1] > thd:
                    y_predict.append(1)
                else:
                    y_predict.append(-1)
            
            acc, pre, rec, f1 = get_eval(y_predict, y_test)
            precision = np.append(precision, pre)
            recall = np.append(recall, rec)
        precision_l.append(precision.mean())
        recall_l.append(recall.mean())
    plt.plot(recall_l, precision_l)
    plt.show()


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
    plot_p_r(x, y)
