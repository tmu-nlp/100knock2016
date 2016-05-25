from knock51 import word_punc
from nltk import stem

stemmer = stem.PorterStemmer()

for word in word_punc().split("\n"):
    print("{}\t{}".format(word, stemmer.stem(word)))
