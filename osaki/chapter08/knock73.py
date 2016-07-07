import sys

def rog_learn(c,f):
    import math
    from knock72 import mk_feature
    from nltk import stem
    from collections import defaultdict

    stemmer=stem.PorterStemmer()
    d=defaultdict(lambda:0)
    al=0.6
    count=0
    while(count<c):
        count+=1
        for line in f:#.split("\n"):
            y=line.split(" ")[0]
            x=mk_feature(line)
            score=0
            for key,value in x.items():
                score+=d[key]*value
            if y=="+1":
                y=1
            elif y=="-1":
                y=-1
            dp_dw=y*math.exp(score)/((1+math.exp(score))**2)
            for key,value in x.items():
                d[key]+=dp_dw*value*al
        al=al*0.8
    return d

if __name__=="__main__":
    s=""
    d=rog_learn(int(sys.argv[1]),open(sys.argv[2]))
    for key,value in d.items():
        print(key+"\t"+str(value))
