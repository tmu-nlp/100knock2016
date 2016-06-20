from knock73 import getFeatureMatrix
from sklearn.externals import joblib


def main():
    lr = joblib.load('./lr.pkl')
    feature_matrix, label_vector = getFeatureMatrix('sentiment.txt')
    with open('sentiment_prediction.txt', 'w') as fp:
        for sentiment, prob in zip(lr.predict(feature_matrix), lr.predict_proba(feature_matrix)):
            print('{}\t{}'.format(sentiment, prob), file=fp)

if __name__ == '__main__':
    main()
