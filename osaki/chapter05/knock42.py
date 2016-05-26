#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=""
t=""
c=0
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        d=int(phrase.dst)
        for word in phrase.morph:
            if word.pos!="記号":
                s+=word.surface
        for phrase_d in line:
            if c==d:
                for word in phrase_d.morph:
                    if word.pos!="記号":
                         t+=word.surface
            c+=1
        c=0
        print(s+"\t"+t)
        s=""
        t=""
