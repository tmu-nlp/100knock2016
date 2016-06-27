from knock72 import getFeature
from sklearn.feature_extraction import DictVectorizer
from sklearn.externals import joblib


def main():
    lr = joblib.load('./lr.pkl')
    dic2vec = DictVectorizer()
    features = list()
    y = list()
    for line in open('sentiment.txt'):
        word_list = line[3:].strip('\n').strip().split()
        features.append(getFeature(word_list))
    x = dic2vec.fit_transform(features)
    with open('sentiment_prediction.txt', 'w') as fp:
        for sentiment, prob in zip(lr.predict(x), lr.predict_proba(x)):
            print('{}\t{}'.format(sentiment, prob), file=fp)

if __name__ == '__main__':
    main()
