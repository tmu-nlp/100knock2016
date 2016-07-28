from gensim.models import word2vec
import math
import numpy as np

X=np.load("../chapter09/knock85.npy")
model=word2vec.Word2Vec.load("knock90.model")
ids=dict()

for line in open("ids_t.txt","r"):
    ids[line.strip("\n").split("\t")[0]]=int(line.strip("\n").split("\t")[1])

f=open("knock94_09.txt","w")
for line in open("wordsim353/set1.tab","r"):
    words=line.split()[:2]
    if words[0] in ids and words[1] in ids:
        v1=X[ids[words[0]]]
        v2=X[ids[words[1]]]
        result=np.dot(v1,v2)/math.sqrt(np.dot(v1,v1.T)*np.dot(v2,v2.T))
    else:
        result="None"
    f.write("\t".join(words)+"\t"+str(result)+"\n")
f.close()

f=open("knock94_10.txt","w")
for line in open("wordsim353/set1.tab","r"):
    words=line.split()[:2]
    if words[0] in model and words[1] in model:
        result=model.similarity(words[0],words[1])
    else:
        result="None"
    f.write("\t".join(words)+"\t"+str(result)+"\n")
f.close()
