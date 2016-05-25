#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

def mkpass(line,n):
    s=""
    l=[]
    l=line[n].morph
    for item in l:
        if item.pos!="記号":
            s+=item.surface
    if line[n].dst=="-1":
        return(s)
    else:
        return(s+" -> "+mkpass(line,int(line[n].dst)))

for line in mkChunkclass(mkMorphclass()):
    for i in range(len(line)):
        if line[i].dst!="-1":
            print(mkpass(line,i))
