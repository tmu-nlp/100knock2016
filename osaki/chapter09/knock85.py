import sys
import numpy as np
from scipy.sparse import lil_matrix,csr_matrix
from scipy.sparse.linalg import svds

ids_t=dict()
ids_c=dict()

f_t=open("knock85_t.txt","w")
f_c=open("knock85_c.txt","w")
for line in open(sys.argv[1]):
    item=line.strip("\n").split("\t")
    if not item[0] in ids_t:
        ids_t[item[0]]=len(ids_t)
        f_t.write(item[0]+"\t"+str(len(ids_t))+"\n")
    if not item[1] in ids_c:
        ids_c[item[1]]=len(ids_c)
        f_c.write(item[0]+"\t"+str(len(ids_c))+"\n")
f_t.close()
f_c.close()

X=lil_matrix((len(ids_t),len(ids_c)))

for line in open(sys.argv[1]):
    item=line.strip("\n").split("\t")
    X[ids_t[item[0]]-1,ids_c[item[1]]-1]=float(item[2])

X_svd=svds(X,300)
X_pca=np.dot(X_svd[0],np.diag(X_svd[1]))

print(X)
np.save("knock85",X_pca)
