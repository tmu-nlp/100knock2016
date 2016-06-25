from nltk.corpus import stopwords


def isStopWords(word):
    stopset = set(stopwords.words('english'))

    with open('stop_words') as fp:
        stopword_gla = fp.read().strip().split('\n')

    stopset.update(stopword_gla)

    if word in stopset:
        return True
    else:
        return False


def main():
    print(isStopWords('a'))
    print(isStopWords('walk'))


if __name__ == '__main__':
    main()
