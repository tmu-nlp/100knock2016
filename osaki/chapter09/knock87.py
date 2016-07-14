import numpy as np

X=np.load("knock85.npy")

ids_t=dict()
ids_c=dict()

for line in open("ids_t.txt","r"):
    ids_t[line.strip("\n").split("\t")[0]]=int(line.strip("\n").split("\t")[1])

v1=X[ids_t["United_States"]]
v2=X[ids_t["U.S"]]

print(np.dot(v1,v2)/(np.dot(v1,v1.T)*np.dot(v2,v2.T)))
