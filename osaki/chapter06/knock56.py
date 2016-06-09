import re
from xml.etree import ElementTree
import sys

tree=ElementTree.parse(sys.argv[1])
root=tree.getroot() 

src=[]
sentences=[]
coreferences=[]
mentions=[]
tags={}
tokens=[]
referenceslist=[]

for sentence in root[0][0]:
    for token in sentence[0]:
        sentences.append(token[0].text)
    src.append(sentences)
    sentences=[]

for coreference in root[0][1]:
    for mention in coreference:
        b=mention.attrib
        if b.keys():
            tags["representative"]=b['representative']
        for m in mention:
            tags[m.tag]=m.text
        mentions.append(tags)
        tags={} 
    coreferences.append(mentions)
    mentions=[]

for coreferencex in coreferences:
    for mentionx in coreferencex:
        if "representative" in mentionx:
            representative_text=mentionx["text"]
            representative_text="「"+representative_text+"("
        else:
            referenceslist.append([mentionx["sentence"],mentionx["start"],representative_text])
            referenceslist.append([mentionx["sentence"],mentionx["end"],")」"])

n=1
m=1
for sentence in src:
    for tokens in sentence:
        for x in referenceslist:
            if int(x[0])==n and int(x[1])==m:
                print(x[2],end="")
        tokens=tokens.replace(r'-LRB-',r'(')
        tokens=tokens.replace(r'-RRB-',r')')
        print(tokens,end=" ")
        m+=1
    print("")
    m=1
    n+=1
