from knock71 import stop
from collections import defaultdict
from nltk import stem

stemming = stem.PorterStemmer()

posinega = defaultdict(int)
for line in open('sentiment.txt'):
    word_list = line.strip('\n').split()
    polarity = int(word_list.pop(0))
    for word in word_list:
        word = stemming.stem(word)
        if stop(word) == False:
            posinega[word] += polarity

for key, value in sorted(posinega.items(), key = lambda x:x[1]):
    print(key + '\t' + str(value))
        
