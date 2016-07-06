from knock71 import stop
from collections import defaultdict
from nltk import stem

stemming = stem.PorterStemmer()

feature_dict = defaultdict(int)
for line in open('sentiment.txt'):
    word_list = line.strip('\n').split()
    word_list.pop(0)
    for word in word_list:
        word = stemming.stem(word)
        if stop(word) == False:
            feature_dict[word] += 1

for word, freq in sorted(feature_dict.items()):
    print(word + '\t' + str(freq))
        
