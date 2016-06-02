from knock51 import getword
import re
from nltk import stem

if __name__ == "__main__":
    word_list = getword()
    stemmer = stem.PorterStemmer()
    for word in word_list:
        print (stemmer.stem(word))
