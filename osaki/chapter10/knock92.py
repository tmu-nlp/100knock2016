from gensim.models import word2vec
import numpy as np
import math

X=np.load("../chapter09/knock85.npy")
model=word2vec.Word2Vec.load("knock90.model")
ids_t=dict()
for line in open("ids_t.txt","r"):
    ids_t[line.strip("\n").split("\t")[0]]=int(line.strip("\n").split("\t")[1])

f=open("knock92_09.txt","w")
for line in open("knock91.txt","r"):
    result="None"
    best=-1
    words=line.strip("\n").split(" ")[:3]
    if words[0] in ids_t and words[1] in ids_t and words[2] in ids_t:
        v1=X[ids_t[words[1]]]-X[ids_t[words[0]]]+X[ids_t[words[2]]]
        for key,value in ids_t.items():
            v2=X[value]
            ans=np.dot(v1,v2)/math.sqrt(np.dot(v1,v1.T)*np.dot(v2,v2.T))
            if ans > best:
                best=ans
                result=key
    f.write(line.strip("\n")+" "+result+" "+str(best)+"\n")
f.close() 

f=open("knock92_10.txt","w")
for line in open("knock91.txt","r"):
    result="None"
    words=line.strip("\n").split(" ")[:3]
    if words[0] in model and words[1] in model and words[2] in model:
        best=result=model.most_similar(positive=[words[1],words[2]],negative=[words[0]])[0][1]
        result=model.most_similar(positive=[words[1],words[2]],negative=[words[0]])[0][0] 
    f.write(line.strip("\n")+" "+result+" "+str(best)+"\n")
f.close()
