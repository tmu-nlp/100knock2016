#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass
import sys

c=0
s=""
t=""
for line in mkChunkclass(mkMorphclass()):
    dot="digraph{\n"
    c+=1
    for phrase in line:
        d=int(phrase.dst)
        for word in phrase.morph:
            if word.pos!="記号":
                s+=word.surface
                dst=phrase.dst
        for phrase_d in line:
            if int(phrase_d.srcs)==d:
                for word in phrase_d.morph:
                    if word.pos!="記号":
                         t+=word.surface
        if dst!="-1":
            dot+="\t"+'"'+s+'"'+" -> "+'"'+t+'"'+";\n"
        s=""
        t=""
    dot+="}"
    if c==int(sys.argv[1]):
        break

f=open("dst.dot","w")
f.write(dot)
f.close
