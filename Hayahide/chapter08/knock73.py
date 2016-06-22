from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.externals import joblib
from nltk import stem
from knock71 import stop

def feature_making(sentence):
    stemming = stem.PorterStemmer()
    ans_list = list()
    for word in sentence:
        word = stemming.stem(word)
        if stop(word) == False:
            ans_list.append(word)
    return ans_list


def feature_vector(feature_list, sentence):
    vector = list()
    for word in feature_list:
        vector.append(1) if word in sentence else vector.append(0)
    return vector


if __name__ == '__main__':
    feature_list = list()
    for line in open('knock72_result.txt'):
        word, value = line.split('\t')
        feature_list.append(word)

    polarity = list()
    feature = list()
    for line in open('sentiment.txt'):
        sentence = line.strip('\n').split()
        polar = sentence.pop(0)
        polarity.append(int(polar))
        sentence = feature_making(sentence)
        feature.append(feature_vector(feature_list, sentence))

    LR = LogisticRegression(C = 1000)
    LR.fit(feature, polarity)
    joblib.dump(LR, 'LR.pkl')
