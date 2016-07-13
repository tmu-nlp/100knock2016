import numpy as np

X=np.load("knock85.npy")

ids_t=dict()

for line in open("ids_t.txt","r"):
    ids_t[line.strip("\n").split("\t")[0]]=int(line.strip("\n").split("\t")[1])

print(X[ids_t["United_States"]])
