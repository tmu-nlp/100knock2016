import sys
from collections import defaultdict

d_tc=defaultdict(lambda:0)
d_t=defaultdict(lambda:0)
d_c=defaultdict(lambda:0)
N=0
for line in open(sys.argv[1]):
    tokens=line.strip("\n")
    d_tc[tokens]+=1
    d_t[tokens.split("\t")[0]]+=1
    d_c[tokens.split("\t")[1]]+=1
    N+=1

with open("knock83_tc.txt","w") as f_tc:
    for key,value in d_tc.items():
        f_tc.write(key+"\t"+str(value)+"\n")

with open("knock83_t.txt","w") as f_t:
    for key,value in d_t.items():
        f_t.write(key+"\t"+str(value)+"\n")

with open("knock83_c.txt","w") as f_c:
    for key,value in d_c.items():
        f_c.write(key+"\t"+str(value)+"\n")

open("knock83_n.txt","w").write(str(N))
