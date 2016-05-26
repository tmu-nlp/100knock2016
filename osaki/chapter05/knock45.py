#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=[]
t=[]
result=""
wordtt=[]
c=0
cs=0
test=0
for line in mkChunkclass(mkMorphclass()):
    test+=1
    for phrase in line:
        d=cs
        for word in phrase.morph:
            if word.pos!="記号":
                s+=[[word.pos,word.base]]
        for phrase_d in line:
            if int(phrase_d.dst)==d:
                for word in phrase_d.morph:
                    if word.pos!="記号":
                        t+=[[word.pos,word.base]]
            c+=1
        c=0
        for words in s:
            if words[0]=="動詞":
                result+=words[1]+"\t"
                for wordt in t:
                    if wordt[0]=="助詞":
                        wordtt+=[wordt[1]]
                result+=" ".join(sorted(wordtt))
                print(result.strip(" "))
                result=""
                wordtt=[]
        s=[]
        t=[]
        cs+=1
    cs=0
    if test==8:
        break
