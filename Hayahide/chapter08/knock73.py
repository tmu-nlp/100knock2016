from collections import defaultdict
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
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


def feature_vector(sentence):
    vector = defaultdict(int)
    for word in sentence:
        vector[word] += 1
    return vector


if __name__ == '__main__':
    polarity = list()
    feature = list()
    dicvec = DictVectorizer()
    for line in open('sentiment.txt'):
        sentence = line.strip('\n').split()
        polar = sentence.pop(0)
        polarity.append(int(polar))
        sent_feature = feature_making(sentence)
        feature.append(feature_vector(sent_feature))
    x_feature = dicvec.fit_transform(feature)

    LR = LogisticRegression()
    LR.fit(x_feature, polarity)
    joblib.dump(LR, 'LR.pkl')
