import sys
from xml.etree.ElementTree import *
from collections import defaultdict

tree=parse(sys.argv[1])
elem=tree.getroot()

word=[]
line=[]
sentence=[]

for e in elem[0][0]:
    for words in e[0]:
        line+=[words[0].text]
    sentence+=[line]
    line=[]

dn=[]
dd=[]
dnlist=[]
ddlist=[]
for e in elem[0][0]:
    for item in e[2]:
        if item.get("type")=="dobj":
            dd+=[[item.find("governor").get("idx"),item.findtext("governor"),item.findtext("dependent")]]
        elif item.get("type")=="nsubj":
            dn+=[[item.find("governor").get("idx"),item.findtext("governor"),item.findtext("dependent")]]
    dnlist+=[dn]
    ddlist+=[dd]
    dn=[]
    dd=[]

for (line_n,line_d) in zip(dnlist,ddlist):
    for item_n in line_n:
        for item_d in line_d:
            if item_n[0]==item_d[0]:
                print(item_n[1]+"\t"+item_n[2]+"\t"+item_d[2])
