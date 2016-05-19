#-*- coding:utf-8 -*-
import re
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
d=defaultdict(lambda:0)
dw=defaultdict(lambda:0)
dh=defaultdict(lambda:0)
dc=defaultdict(lambda:0)
l=list()
lhx=list()
lhy=list()
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
    dw[words["基本形"]]=dw[words["基本形"]]+1
for foo,bar in dw.items():
    dh[bar]=dh[bar]+1
for foo,bar in sorted(dh.items(),key=lambda x:x[0]):
    lhx+=[foo]
    lhy+=[bar]
plt.figure(figsize=(16,6))
plt.bar(lhx,lhy)
plt.show()
