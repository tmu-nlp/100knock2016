from gensim.models import word2vec
import sys
sys.path.append("/Users/Yukio/work/100kcnok2016/yukio/chapter09/")
from knock86 import knock_86
from knock87 import knock_87
from knock88 import knock_88
from knock89 import knock_89

data = word2vec.Text8Corpus("../chapter09/tokens_81.txt")
model = word2vec.Word2Vec(data, size = 300)
model.save("word2vec")

vec = {}
for word in model.vocab.keys():
    vec[word] = model[word]

print("knock86")
knock_86(vec)
print()
print("knock87")
knock_87(vec)
print()
print("knock88")
knock_88(vec)
print()
print("knock89")
knock_89(vec)
print()
