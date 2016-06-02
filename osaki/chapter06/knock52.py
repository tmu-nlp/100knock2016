from knock50 import mkline
from knock51 import mkword
from nltk import stem
import sys
import re

for line in open(sys.argv[1]):
    for sentence in mkline(line).strip("\n").split("\n"):
        for word in mkword(sentence).split("\n"):
            stemmer=stem.PorterStemmer()
            word_stem=stemmer.stem(word)
            print(word+"\t"+word_stem)
