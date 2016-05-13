#-*- coding:utf-8 -*-
import re
from collections import defaultdict
d=defaultdict(lambda:0)
l=list()
c=0
s=""
for line in open("neko.txt.mecab","r"):
    if line == "EOS\n":
        continue
    line=re.sub(",,*",",",line.replace("\t"," ").replace(" ",","))
    d={}
    d["表層形"]=line.split(",")[0]
    d["基本形"]=line.split(",")[-3]
    d["品詞"]=line.split(",")[1]
    d["品詞細分類１"]=line.split(",")[2]
    l.append(d)

for words in l:
    if words["品詞"]=="名詞":
        s+=words["表層形"]
        c+=1
    else:
        if c>=2:
            print(s)
        s=""
        c=0
