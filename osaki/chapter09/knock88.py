import numpy as np
import math

X=np.load("knock85.npy")

ids_t=dict()
d=dict()

for line in open("ids_t.txt","r"):
    ids_t[line.strip("\n").split("\t")[0]]=int(line.strip("\n").split("\t")[1])

v1=X[ids_t["United_States"]]

for key,value in ids_t.items():
    v2=X[value]
    d[key]=np.dot(v1,v2)/math.sqrt(np.dot(v1,v1.T)*np.dot(v2,v2.T))

c=0
for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
    c+=1
    print(key,value)
    if c==10:
        break
