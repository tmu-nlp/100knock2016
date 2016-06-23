#-*- coding:utf-8 -*-
import random

l=list()

for line in open("rt-polarity.pos","rb"):
    l+=["+1 "+line.decode("iso8859")]
for line in open("rt-polarity.neg","rb"):
    l+=["-1 "+line.decode("iso8859")]

random.shuffle(l)

with open("sentiment.txt","w") as f:
    for item in l:
        f.write(item)

c_p=0
c_n=0
for line in open("sentiment.txt","r"):
    if line.split(" ")[0]=="+1":
        c_p+=1
    else:
        c_n+=1
print(str(c_p)+"\t"+str(c_n))
