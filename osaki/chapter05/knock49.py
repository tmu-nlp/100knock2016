#-*- coding:utf-8 -*-
from knock40 import mkMorphclass
from knock41 import mkChunkclass

def mkpass(line,n,m):
    s=""
    l=[]
    l=line[n].morph
    for item in l:
        if item.pos!="記号":
            s+=item.surface
    if n==m:
        return("|"+s)
    elif m!=-1 and line[n].dst=="-1":
        return("|"+mkpass(line,int(line[m].dst),n))
    else:
        return(" -> "+s+mkpass(line,int(line[n].dst),m))

def mk_i_j(line,n,m):
    s=""
    t=""
    for item in line[n].morph:
        if item.pos=="名詞":
            s+="Ｘ"
        else:
            s+=item.surface
    for item in line[m].morph:
        if item.pos=="名詞":
            t+="Ｙ"
        else:
            t+=item.surface
    return ([s,t])

test=0
for line in mkChunkclass(mkMorphclass()):
    test+=1
    for i in range(len(line)):
        c=0
        for item in line[i].morph:
            if item.pos=="名詞":
              c+=1
        if line[i].dst!="-1" and c>=1:
            for j in range(i+1,len(line)):
                for item in line[j].morph:
                    if item.pos=="名詞":
                        if len(mkpass(line,int(line[i].dst),j).split("|"))<=2:
                            print(mk_i_j(line,i,j)[0]+mkpass(line,int(line[i].dst),j).split("|")[0]+" -> "+mk_i_j(line,i,j)[1])
                        else:
                            print(mk_i_j(line,i,j)[0]+mkpass(line,int(line[i].dst),j).split("|")[0]+"|"+mk_i_j(line,i,j)[1]+mkpass(line,int(line[i].dst),j).split("|")[1]+"|"+mkpass(line,int(line[i].dst),j).split("|")[2])
#    if test==8:
#        break
