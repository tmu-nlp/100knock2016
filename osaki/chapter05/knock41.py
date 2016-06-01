#-*- coding:utf-8 -*-

class Chunk:
    def __init__(self,morph,dst,srcs):
        self.morph=morph
        self.dst=dst
        self.srcs=srcs
    def __str__(self):
        morph_=[str(i) for i in self.morph]
        srcs_=[str(i) for i in self.srcs]
        return(" ".join(morph_)+" || "+self.dst+" || "+",".join(srcs_))

def mkChunkclass(morphlist):
    import re
    l=list()
    l_=list()
    la=list()
    morph=list()
    c1=0
    c2=0
    cs=0
    dst=""
    srcs=[]
    for line in open("neko.txt.cabocha","r"):
        if line.startswith("EOS")==True:
            c1+=1
            chunk=Chunk(morph,dst,srcs)
            l+=[chunk]
            srcs=[]
            morph=[]
            la+=[l]
            l=list()
            l_=list()
            c2=0
        elif line.startswith("*")==True:
            if c2!=0:
                chunk=Chunk(morph,dst,srcs)
                l+=[chunk]
                morph=[]
                srcs=[]
            for item in l:
                if item.dst==line.split(" ")[1]:
                    srcs+=[str(cs)]
                cs+=1
            cs=0
            dst=line.split(" ")[2].strip("D")
        else:
            morph+=[morphlist[c1][c2]]
            c2+=1
    return(la)

if __name__=="__main__":
    from knock40 import mkMorphclass
    c=0
    for l in mkChunkclass(mkMorphclass()):
        c+=1
        if c==8:
            for ch in l:
                print(ch)
