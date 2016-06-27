import sys
from nltk.corpus import stopwords


def if_stopword(word):
    stop_list = stopwords.words("english") + [",",".","!","?",";",":","\n","\t","(",")"," ",""]
    if word.lower() in stop_list:
        return True
    else:
        return False


if __name__ == '__main__':
    print(if_stopword(sys.argv[1]))
