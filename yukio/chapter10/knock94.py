from gensim.models import word2vec
import pickle
import sys
sys.path.append("/Users/Yukio/work/100kcnok2016/yukio/chapter09/")
from knock87 import cos_sim

with open("../chapter09/word_vec_85.pickle", "rb") as f:
    vec_85 = pickle.load(f)

vec_90 = word2vec.Word2Vec.load("word2vec")

f_85 = open("result_94_v85.txt", "w")
f_90 = open("result_94_v90.txt", "w")

for i, line in enumerate(open("combined.tab")):
    if i != 0:
        word1, word2, val = line.strip().split()

        if word1 in vec_85 and word2 in vec_85:
            f_85.write("{}\t{}\n".format(line.strip(), cos_sim(vec_85[word1], vec_85[word2])))

        if word1 in vec_90.vocab.keys() and word2 in vec_90.vocab.keys():
            f_90.write("{}\t{}\n".format(line.strip(), cos_sim(vec_90[word1], vec_90[word2])))

f_85.close()
f_90.close()

