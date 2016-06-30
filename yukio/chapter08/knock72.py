from knock71 import include_stopword
from collections import defaultdict
from nltk import stem

def extract_feature(sentence):
    features = defaultdict(lambda: 0)
    stemmer = stem.PorterStemmer()
    for word in sentence.split():
        if not include_stopword(word):
            features[stemmer.stem(word)] += 1
    return features

label_list = []
features_list = []

for line in open("sentiment.txt", "r"):
    label_list.append(int(line[:2]))
    features_list.append(extract_feature(line[3:]))

if __name__ == "__main__":
    for label, features in zip(label_list, features_list):
        print("{} {}".format(label, dict(features)))
