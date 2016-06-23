# -*- coding: utf-8 -
from nltk.corpus import stopwords

def getstopword():
    stoplist = stopwords.words('english') #エラー出たからimport nltk > nltk.download()でall-corpora
    stoplist.append(',')
    return stoplist

def search_stop(word):
    if word in getstopword():
        return True
    else:
        return False

if __name__ == "__main__":
    print (search_stop('is'))
    print (search_stop('such'))
    print (search_stop('interesting'))