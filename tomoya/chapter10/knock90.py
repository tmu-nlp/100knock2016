from gensim.models import word2vec
import os
import sys
sys.path.append("/Users/tomoya/Work/100knock2016/tomoya/chapter09")
from knock86 import knock86
from knock87 import knock87
from knock88 import knock88
from knock89 import knock89

def main():
    sentences = word2vec.Text8Corpus("./enwiki-corpus2.txt")
    if "knock90.model" in os.listdir("/Users/tomoya/Work/100knock2016/tomoya/chapter10/"):
        model = word2vec.Word2Vec.load("knock90.model")
    else:
        model = word2vec.Word2Vec(sentences, size=300)
        model.save("knock90.model")

    vec = {}
    for word in model.vocab.keys():
        vec[word] = model[word]

    print("knock86.py")
    print(knock86(vec), end='\n\n')
    print("knock87.py")
    print(knock87(vec), end='\n\n')
    print("knock88.py")
    for word in knock88(vec):
        print(word)
    print()
    print("knock89.py")
    for word in knock89(vec):
        print(word)

if __name__ == '__main__':
    main()
