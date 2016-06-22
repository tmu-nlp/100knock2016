import sys
import math 
from collections import defaultdict
from nltk import stem

d=defaultdict(lambda:0)
stemmer=stem.PorterStemmer()

for line in open(sys.argv[1]):
    data=line.strip("\n").split("\t")
    d[data[0]]=float(data[1])

for line in open(sys.argv[2]):
   score=0
   for item in line.strip("\n").split(" "):
       item=stemmer.stem(item)
       score+=d[item]
   p_pos=math.exp(score)/(1+math.exp(score))
   if p_pos > 0.5:
       print("+1 "+line.strip("\n"))
   else:
       print("-1 "+line.strip("\n"))
