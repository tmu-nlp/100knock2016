from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.cross_validation import KFold
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from knock73 import feature_making, feature_vector
from knock74 import fit_feature


def prediction(LR, query, threshold):
    prob = LR.predict_proba(query)[0]
    return -1 if prob[0] > threshold else 1


def cv_prediction(feature_dict, feature, polarity, threshold, folds):
    accuracy = 0
    precision = 0
    recall = 0
    f1 = 0
    count = 0
    dicvec = DictVectorizer()
    LR = LogisticRegression()
    kfold = KFold(len(polarity), n_folds=folds)
    for train, test in kfold:
        count += 1
        x = list()
        y = list()
        [x.append(feature[i]) for i in train]
        [y.append(polarity[i]) for i in train]
        x.append(feature_dict)
        y.append(0)
        LR.fit(dicvec.fit_transform(x), y)
        test_label = list()
        answer_label = list()
        [answer_label.append(polarity[j]) for j in test]
        for j in test:
            query = fit_feature(feature[j], feature_dict)
            result = -1 if query.shape[1] != len(feature_dict) else prediction(LR, query, threshold)
            test_label.append(result)
        accuracy += accuracy_score(answer_label, test_label)
        precision += precision_score(answer_label, test_label)
        recall += recall_score(answer_label, test_label)
        f1 += f1_score(answer_label, test_label)
        print('{}_fold finished.'.format(count))

    return accuracy, precision, recall, f1

if __name__ == '__main__':
    feature_dict = defaultdict(int)
    for line in open('knock72_result.txt'):
        word, value = line.strip('\n').split('\t')
        feature_dict[word] = int(value)

    polarity = list()
    feature = list()
    for line in open('sentiment.txt'):
        sentence = line.strip('\n').split()
        polarity.append(int(sentence.pop(0)))
        feature.append(feature_vector(feature_making(sentence)))

    threshold = 0.5
    folds = 5
    accuracy, precision, recall, f1 = cv_prediction(feature_dict, feature, polarity, threshold, folds)
    print('accuracy: {}'.format(accuracy / 5))
    print('precision: {}'.format(precision / 5))
    print('recall: {}'.format(recall / 5))
    print('F1: {}'.format(f1 / 5))
