#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=[]
t=[]
result=""
wordtt=[]
wordtp=[]
wordtp_=[]
wordtw=[]
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        d=int(phrase.srcs)
        for word in phrase.morph:
            if word.pos!="記号":
                s+=[word]
        for phrase_d in line:
            if int(phrase_d.dst)==d:
                t+=[phrase_d]
        for words in s:
            if words.pos=="動詞":
                result+=words.base+"\t"
                for wordt_ in t:
                    for wordt in wordt_.morph:
                        if wordt.pos=="助詞":
                            wordtt+=[[wordt.base,wordt_]]
                wordtt=sorted(wordtt,key=lambda x:x[0])
                for item in wordtt:
                    for word in item[1].morph:
                        if word.pos!="記号":
                            wordtp_+=[word.surface]
                    wordtp+=["".join(wordtp_)]
                    wordtp_=[]
                    wordtw+=[item[0]]
                result+=" ".join(wordtw)
                result+="\t"
                result+=" ".join(wordtp)
                print(result)
                result=""
                wordtt=[]
                wordtp=[]
                wordtw=[]
        s=[]
        t=[]
