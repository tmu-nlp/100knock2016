import sys
import math
from knock72 import mk_feature
from nltk.corpus import stopwords
from nltk import stem

stemmer=stem.PorterStemmer()
stoplist=stopwords.words("english")+[",",".","!","?",";",":","\n","\t","(",")"," "]

d_f=mk_feature()
d={}
al=0.6

for key,value in d_f.items():
    d[key]=0

count=0
while(count<int(sys.argv[1])):
    count+=1
    for line in open("sentiment.txt","r"):
        y=float(line.split(" ")[0])
        x=list()
        score=0
        for item in line.strip("\n").split(" ")[1:]:
            item=stemmer.stem(item)
            if item not in stoplist:
                if item in d:
                    score+=d[item]
                    x+=[item]
        dp_dw=y*math.exp(score)/((1+math.exp(score))**2)
        for item in x:
            d[item]+=dp_dw*al
    al=al*0.8

for key,value in d.items():
    print(key+"\t"+str(value))
