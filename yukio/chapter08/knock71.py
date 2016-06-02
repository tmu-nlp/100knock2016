import sys
from nltk.corpus import stopwords

def include_stop_word(word):
    stop_word = stopwords.words("english")
    print(stop_word)
    if word in stop_word:
        return True
    else:
        return False

if __name__ == "__main__":
    print(include_stop_word(sys.argv[1]))
