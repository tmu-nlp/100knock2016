from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib
from knock72 import get_feature
from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
import numpy as np
from collections import *
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

logreg = LogisticRegression()
word_vec = DictVectorizer()
folds = 5

def make_kfold(target, feature):
    preds = []
    kf = KFold(len(target), n_folds=folds,shuffle=True)
    test_numbers = []
    for trains, tests in kf:
        test_numbers.append(tests)
        pred_list = []
        feature_list = word_vec.fit_transform([dict(Counter(feature[train])) for train in trains])
        target_list = [target[train] for train in trains]
        logreg.fit(feature_list, target_list)
        for test in tests:
            feature_dict = defaultdict(int)
            for f in word_vec.get_feature_names():
                feature_dict[f] = 0
            for key, value in dict(Counter(feature[test])).items():
                if key in feature_dict:
                    feature_dict[key] = value
            pred_list.append(feature_dict)
        preds.append(logreg.predict(word_vec.fit_transform(pred_list)))
    return preds, test_numbers

def get_score(preds, target, test_numbers):
    all_accuracy = []
    all_precision = []
    all_recall = []
    all_f_values = []
    for tests, pred in zip(test_numbers, preds):
        answers = []
        for test in tests:
            answers.append(target[test])
        all_accuracy.append(accuracy_score(answers, pred))
        all_precision.append(precision_score(answers, pred))
        all_recall.append(recall_score(answers, pred))
        all_f_values.append(f1_score(answers, pred))
    return np.array(all_accuracy).mean(), np.array(all_precision).mean(), np.array(all_recall).mean(), np.array(all_f_values).mean()

if __name__ == '__main__':
    target, feature = get_feature()
    preds, test_numbers = make_kfold(target, feature)
    print("正解率:{}\t適合率:{}\t再現率:{}\tF1スコア:{}".format(*get_score(preds, target, test_numbers)))
