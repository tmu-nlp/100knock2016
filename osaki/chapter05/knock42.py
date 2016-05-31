#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=""
t=""
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        d=int(phrase.dst)
        for word in phrase.morph:
            if word.pos!="記号":
                s+=word.surface
        for word in line[d].morph:
            if word.pos!="記号":
                 t+=word.surface
        print(s+"\t"+t)
        s=""
        t=""
