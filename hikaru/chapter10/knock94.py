from gensim.models import word2vec
import pickle
import scipy.spatial.distance as dis
import numpy as np

f = open("knock94.txt", "w")
model = word2vec.Word2Vec.load("knock90_word2vec")
unk_list = list()
Flag = False
for line in open("combined.tab"):
    if Flag == True:
        word1, word2, value = line.strip("\n").split("\t")
        if word1 in model and word2 in model:
            sim = model.similarity(word1, word2)
            f.write("{} {} {} {}\n".format(word1, word2, value, sim))
        else:
            f.write("{} {} {} 0.50\n".format(word1, word2, value))
            if word1 not in model:
                unk_list.append(word1)
            if word2 not in model:
                unk_list.append(word2)
    Flag = True
print (set(unk_list))
f.close()

#-------------------------------------------------
'''
f = open("knock94_85.txt", "w")
model_85 = pickle.load(open('X_dict.pickle', mode='rb'))
unk_list = list()
Flag = False
for line in open("combined.tab"):
    if Flag == True:
        word1, word2, value = line.strip("\n").split("\t")
        if word1 in model_85 and word2 in model_85 and model_85[word1] == np.zeros(300) and model_85[word2] == np.zeros(300): ##???
            sim = 1 - dis.cosine(model_85[word1], model_85[word2])
            f.write("{} {} {} {}\n".format(word1, word2, value, sim))
        else:
            f.write("{} {} {} 0.50\n".format(word1, word2, value))
            if word1 not in model:
                unk_list.append(word1)
            if word2 not in model:
                unk_list.append(word2)
    Flag = True
print (set(unk_list))
f.close()
'''
