import sys
from collections import defaultdict
from knock73 import rog_learn
from knock77 import acc_

c=0
k=[""]*5
for line in open(sys.argv[1]):
    c+=1
    k[c%5]+=line

for i in range(len(k)):
    train=k[i].strip("\n")
    d=rog_learn(10,train)
    k_4=k[:i]+k[i+1:]
    test="\n".join(k_4).strip("\n")
    print(acc_(test,d,0.5))
