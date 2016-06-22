import sys 
from collections import defaultdict
from nltk import stem

d=defaultdict(lambda:0)
stemmer=stem.PorterStemmer()

for line in open(sys.argv[1]):
    data=line.strip("\n").split("\t")
    d[data[0]]=float(data[1])

for line in open(sys.argv[2]):
   prob=0
   for item in line.strip("\n").split(" "):
       item=stemmer.stem(item)
       prob+=d[item]
   print(prob)
   if prob>0:
       print("+1 "+line.strip("\n"))
   else:
       print("-1 "+line.strip("\n"))
