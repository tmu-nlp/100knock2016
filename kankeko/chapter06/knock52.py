from stemming.porter2 import stem
from knock51 import get_word


def word_stem():
    for word in get_word():
        word = word.replace(',', '')
        print(stem(word), '\t', word)

if __name__ == '__main__':
    word_stem()
