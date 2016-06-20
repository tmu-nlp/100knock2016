from knock71 import isStopWords
from nltk import stem
from collections import defaultdict


def getFeature(word_list):
    stemmer = stem.LancasterStemmer()
    # stemmer2 = stem.PorterStemmer()
    feature = list()
    for word in word_list:
        if not isStopWords(word):
            word_stem = stemmer.stem(word)
            if word_stem not in feature:
                feature.append(stemmer.stem(word))
    return feature


def getFeatureList(filename):
    features = list()
    all_feature = list()
    for line in open(filename):
        words = line[3:].strip('\n').strip().split(' ')
        features.append([line[:2], getFeature(words)])
    for y, x in features:
        for feature in x:
            if feature not in all_feature:
                all_feature.append(feature)
    return all_feature, features

if __name__ == '__main__':
    feature_list = getFeatureList('./sentiment.txt')
    print(feature_list[:10])
