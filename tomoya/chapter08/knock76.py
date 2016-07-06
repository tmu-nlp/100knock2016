from knock72 import getFeature
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib


def getLabeledData():
    lr = joblib.load('./lr.pkl')
    dic2vec = DictVectorizer()
    features = list()
    y = list()
    for line in open('sentiment.txt'):
        word_list = line[3:].strip('\n').strip().split()
        label = int(line[:2])
        features.append(getFeature(word_list))
        y.append(label)
    x = dic2vec.fit_transform(features)
    pred_label = lr.predict(x)
    prob = lr.predict_proba(x)
    return y, pred_label, prob


if __name__ == '__main__':
    with open('ref_pred.txt', 'w') as fp:
        for reference, sentiment, prob in zip(*getLabeledData()):
            print('{}\t{}\t{}'.format(reference, sentiment, prob), file=fp)
