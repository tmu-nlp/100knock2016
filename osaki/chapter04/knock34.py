#-*- coding:utf-8 -*-
import re
from collections import defaultdict
d=defaultdict(lambda:0)
l=list()
c=0

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
    if words["表層形"]=="の" and words["品詞"]=="助詞":
        if l[c-1]["品詞"]=="名詞" and l[c+1]["品詞"]=="名詞":
            print(l[c-1]["表層形"]+words["表層形"]+l[c+1]["表層形"])
    c+=1
