import sys
import math
import numpy as np
from scipy.sparse import lil_matrix

d_t=dict()
d_c=dict()
ids_t=dict()
ids_c=dict()


for line in open(sys.argv[2]): #f(t,*)読み込み
    d_t[line.split("\t")[0]]=float(line.strip("\n").split("\t")[1])
    if not line.split("\t")[0] in ids_t:
        ids_t[line.split("\t")[0]]=len(ids_t)-1

for line in open(sys.argv[3]): #f(*,c)読み込み
    d_c[line.split("\t")[0]]=float(line.strip("\n").split("\t")[1])
    if not line.split("\t")[0] in ids_c:
        ids_c[line.split("\t")[0]]=len(ids_c)-1

N=int(open(sys.argv[4]).read())

X=lil_matrix((len(d_t),len(d_c)))

for line in open(sys.argv[1]):
    x=line.strip("\n").split("\t")
    x[2]=float(x[2])
    if x[2]<10:
        x_tc=0
    else:
        x_tc=max(math.log((N*x[2])/(d_t[x[0]]*d_c[x[1]])),0)
    if x_tc!=0:
        X[ids_t[x[0]],ids_c[x[1]]]=x_tc

print(X)
np.save("knock84",X)
