#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

s=[]
t=[]
tf=0
result=""
wordtt=[]
wordtp=[]
wordtp_=[]
wordtw=[]
test=0
c=0
for line in mkChunkclass(mkMorphclass()):
    for phrase in line:
        for item in phrase.srcs:
            if len(line[int(item)].morph)>=2 and line[int(item)].morph[0].pos1=="サ変接続" and line[int(item)].morph[1].base=="を":
                tf+=1
        if tf>=1:
            for word in phrase.morph:
                if word.pos!="記号":
                    s+=[word]
            for item in phrase.srcs:
                    t+=[line[int(item)]]
            for words in s:
                if c==0:
                    if words.pos=="動詞":
                        c+=1
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
                            if item[1].morph[0].pos1=="サ変接続" and item[1].morph[1].base=="を":
                                result="".join(wordtp_)+result
                            else:
                                wordtp+=["".join(wordtp_)]
                                wordtw+=[item[0]]
                            wordtp_=[]
                        result+=" ".join(wordtw)
                        result+="\t"
                        result+=" ".join(wordtp)
                        print(result)
                        result=""
                        wordtt=[]
                        wordtp=[]
                        wordtw=[]
            c=0
            s=[]
            t=[]
        tf=0
    test+=1
#    if test==8:
#        break
