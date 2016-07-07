import sys
from collections import defaultdict

def mk_label(line,d,thre):
    import math
    from nltk import stem
    stemmer=stem.PorterStemmer()

    score=0
    for item in line.strip("\n").split(" "):
        item=stemmer.stem(item)
        score+=d[item]
    p_pos=math.exp(score)/(1+math.exp(score))
    if p_pos > thre:
        return(line.split(" ")[0]+"\t+1\t"+str(p_pos))
    else:
        return(line.split(" ")[0]+"\t-1\t"+str(p_pos))

if __name__=="__main__":
    d=defaultdict(lambda:0)
    for line_d in open("model.txt","r"):
        data=line_d.strip("\n").split("\t")
        d[data[0]]=float(data[1])
    for line in open(sys.argv[1]):
        print(mk_label(line,d,0.5))
