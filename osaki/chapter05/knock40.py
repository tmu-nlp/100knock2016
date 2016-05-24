#-*- coding:utf-8 -*-

def mkMorphclass():
    class Morph:
        def __init__(self,surface,base,pos,pos1):
            self.surface=surface
            self.base=base
            self.pos=pos
            self.pos1=pos1

    import re
    l=list()
    la=list()

    for line in open("neko.txt.cabocha","r"):
        if line.startswith("EOS")==True:
            la+=[l]
            l=list()
        elif line.startswith("*")==False:
            line=re.sub(",,*",",",line.replace("\t"," ").replace(" ",","))
            linelist=line.split(",")
            morph=Morph(linelist[0],linelist[7],linelist[1],linelist[2])
            l+=[morph]
    return(la)

if __name__=='__main__':
    c=0
    for l in mkMorphclass():
        c+=1
        if c==3:
            for m in l:
                print(m)
