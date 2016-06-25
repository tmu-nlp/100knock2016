from knock71 import stop
from collections import defaultdict
from nltk import stem

stemming = stem.PorterStemmer()

feature_list = list()
for line in open('sentiment.txt'):
    word_list = line.strip('\n').split()
    word_list.pop(0)
    for word in word_list:
        word = stemming.stem(word)
        if stop(word) == False:
            feature_list.append(word)

for word in feature_list:
    print(word)
        
