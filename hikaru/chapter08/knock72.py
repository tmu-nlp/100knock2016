# -*- coding: utf-8 -

from nltk import stem
from collections import defaultdict
from knock71 import getstopword

stoplist = getstopword()
stemmer = stem.PorterStemmer()

def create_features(input_file):
    phi = defaultdict(int)
    for line in open(input_file, "r"):
        words = line.strip("\n").split()
        for word in words[1:]:
            word = stemmer.stem(word)
            if word in stoplist:
                pass
            else:
                phi[word] += 1
    return phi

def create_feature_vector(line, features_dict):
    featureline_list = list()
    feature_vector = list()
    words = line.strip("\n").split()
    for word in words[1:]:
        word = stemmer.stem(word)
        if word in stoplist:
            pass
        else:
            featureline_list.append(word)
    for feature, value in features_dict.items():
        if feature in featureline_list:
            feature_vector.append(value)
            #feature_vector.append(1)
        else:
            feature_vector.append(0)
    return feature_vector, int(words[0])


if __name__ == "__main__":
    phi = create_features('sentiment.txt')
    #for key, value in phi.items():
        #print ("{} ------> {}".format(key, value))
    for line in open("sentiment.txt", "r"):
        feature_vector, polarity = create_feature_vector(line, phi)
        print (polarity)