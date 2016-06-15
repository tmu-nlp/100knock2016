import sys
import re
from xml.etree import ElementTree

tree=ElementTree.parse(sys.argv[1])
root=tree.getroot() 

parses=[]
for e in root[0][0]:
    t=re.sub(r"\)",r" )",e[1].text)
    t=re.sub(r"\(",r"( ",t)
    parses+=[t.split(" ")]

n=0
RBcounter=0
for parse in parses:
    for token in parse:
        NPtokenlist=[]
        if token=="NP":
            NPlist=parse[n+1:]
            for NPtoken in NPlist:
                if NPtoken=="(":
                    RBcounter+=1
                elif NPtoken==")":
                    RBcounter-=1
                if RBcounter==-1:
                    print("")
                    break
                NPtokenlist+=[NPtoken]

            LRBflag = 0
            for NPtoken  in NPtokenlist:
                if NPtoken == ")":
                    continue
                elif NPtoken == "(":
                    LRBflag = 1
                    continue
                elif NPtoken != "(" and LRBflag == 1:
                    LRBflag -= 1
                else:
                    if NPtoken == "-LRB-":
                        print("(",end=" ")
                    elif NPtoken == "-RRB-":
                        print(")",end=" ")
                    else:
                        print(NPtoken,end=" ")        
            RBcounter = 0 
        n += 1
    print("")
    n = 0
