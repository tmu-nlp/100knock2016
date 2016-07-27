from gensim.models import word2vec
import numpy as np
import math

data=word2vec.Text8Corpus("knock81.txt")
model=word2vec.Word2Vec(data)
model.save("knock90.model")
#model=word2vec.Word2Vec.load("knock90.model")

print(model["United_States"])

v1=model["United_States"]
v2=model["U.S"]
print(np.dot(v1,v2)/math.sqrt(np.dot(v1,v1.T)*np.dot(v2,v2.T)))
print(model.similarity("United_States","U.S"))

d=dict()
for key in model.vocab.keys():
    v2=model[key]
    d[key]=np.dot(v1,v2)/math.sqrt(np.dot(v1,v1.T)*np.dot(v2,v2.T))
c=0
for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
    if key != "United_States":
        c+=1
        print(key,value)
    if c==10:
        break
print(model.most_similar(positive=["United_States"]))
