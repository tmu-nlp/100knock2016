from gensim.models import word2vec
import pickle
import sys
sys.path.append("/Users/Yukio/work/100kcnok2016/yukio/chapter09/")
from knock87 import cos_sim

with open("../chapter09/word_vec_85.pickle", "rb") as f:
    vec_85 = pickle.load(f)

vec_90 = word2vec.Word2Vec.load("word2vec")

f_85 = open("result_92_v85.txt", "w")
f_90 = open("result_92_v90.txt", "w")

for line in open("data_91.txt"):
    word1, word2, word3, word4 = line.strip().split()

    if word1 in vec_85 and word2 in vec_85 and word3 in vec_85:
        sim_dic = {}
        for token, vector in sorted(vec_85.items()):
            sim_dic[token] = cos_sim(vec_85[word2] - vec_85[word1] + vec_85[word3], vector)
        for (word, sim), i in zip(sorted(sim_dic.items(), key = lambda x: x[1], reverse = True), range(0, 1)):
            f_85.write("{} {} {}\n".format(line.strip(), word, sim))

    if word1 in vec_90.vocab.keys() and word2 in vec_90.vocab.keys() and word3 in vec_90.vocab.keys():
        result = vec_90.most_similar(positive = [word2, word3], negative = [word1])
        for (word, sim), i in zip(result, range(0, 1)):
            f_90.write("{} {} {}\n".format(line.strip(), word, sim))

f_85.close()
f_90.close()

