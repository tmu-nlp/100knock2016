from knock71 import isStopWords
from nltk import stem
from collections import defaultdict


def getFeature(word_list):
    stemmer = stem.LancasterStemmer()
    # stemmer2 = stem.PorterStemmer()
    feature = defaultdict(lambda: 0)
    for word in word_list:
        if not isStopWords(word):
            word_stem = stemmer.stem(word)
            feature[word_stem] += 1
    return dict(feature)


if __name__ == '__main__':
    print(getFeature(['I', 'am', 'a', 'student']))
