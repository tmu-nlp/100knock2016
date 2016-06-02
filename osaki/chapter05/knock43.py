#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=""
t=""
ps=[]
pt=[]
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        for word in phrase.morph:
            if word.pos!="記号":
                s+=word.surface
                ps+=[word.pos]
        for word in line[int(phrase.dst)].morph:
            if word.pos!="記号":  
                t+=word.surface
                pt+=[word.pos]
        if "名詞" in ps and "動詞" in pt:
            print(s+"\t"+t)
        s=""
        t=""
        ps=[]
        pt=[]
