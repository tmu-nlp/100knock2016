from sklearn import cross_validation, grid_search
from sklearn.cross_validation import cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from knock75 import get_feature
from sklearn import metrics
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, precision_recall_curve
from sklearn.metrics import f1_score
import pylab as pl

if __name__ == "__main__":
    features_matrix = list()
    polarity_list = list()
    vec = DictVectorizer()
    for line in open("sentiment.txt", "r"):
        phi, polarity = get_feature(line)
        features_matrix.append(phi)
        polarity_list.append(polarity)
    X = vec.fit_transform(features_matrix)
    parameters = {'C': [0.1, 1, 10, 100, 1000]}
    lr = LogisticRegression()
    clf = grid_search.GridSearchCV(lr, parameters)
    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, polarity_list, test_size=0.2, random_state=None)
    res = clf.fit(X_train, y_train)
    prob = clf.predict_proba(X_test)[:, 1] #????
    precision, recall, thresholds = precision_recall_curve(y_test, prob)

    #recall = metrics.recall_score(polarity_list, predicted)
    #precision = metrics.precision_score(polarity_list, predicted)

    pl.plot(recall, precision, label="Precision-Recall curve")
    pl.xlabel('Recall')
    pl.ylabel('Precision')
    pl.ylim([0.0, 1.05])
    pl.xlim([0.0, 1.0])
    pl.title('Precision-Recall example')
    pl.legend(loc="lower left")
    pl.show()
    print (res.best_params_)

    '''
    clf = LogisticRegression()
    predicted = cross_validation.cross_val_predict(clf, X, polarity_list, cv=5)
    print ('accuracy:{}'.format(metrics.accuracy_score(polarity_list, predicted)))
    print ('precision:{}'.format(metrics.precision_score(polarity_list, predicted)))
    print ('recall:{}'.format(metrics.recall_score(polarity_list, predicted)))
    print ('f:{}'.format(metrics.f1_score(polarity_list, predicted)))
    '''