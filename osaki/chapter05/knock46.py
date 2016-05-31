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
#test=0
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        for word in phrase.morph:
            if word.pos!="記号":
                s+=[word]
        for item in phrase.srcs:
                t+=[line[int(item)]]
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
                if wordtp!=[]:
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
#    test+=1
#    if test==8:
#        break
