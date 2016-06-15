import sys
from nltk.corpus import stopwords

def include_stopword(word):
    return word in stopwords.words("english") + [".", ",", "(", ")", "--"]

if __name__ == "__main__":
    print(include_stopword(sys.argv[1]))
