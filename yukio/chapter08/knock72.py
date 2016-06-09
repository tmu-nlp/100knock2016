from knock71 import include_stopword
from nltk import stem

def extract_feature(sentence):
    features = []
    stemmer = stem.PorterStemmer()
    for word in sentence.split():
        if include_stopword(word) == False:
            features.append(stemmer.stem(word))
    return features

label_list = []
features_list = []

for line in open("sentiment.txt", "r"):
    label_list.append(int(line[:2]))
    features_list.append(extract_feature(line[3:]))

if __name__ == "__main__":
    for label, features in zip(label_list, features_list):
        print("{} {}".format(label, features))
