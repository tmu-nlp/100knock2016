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

#test=0
for line in mkChunkclass(mkMorphclass()):
#    test+=1
    for i in range(len(line)):
        c=0
        for item in line[i].morph:
            if item.pos=="名詞":
              c+=1
        if line[i].dst!="-1" and c>=1:
            print(mkpass(line,i))
#    if test==8:
#        break
