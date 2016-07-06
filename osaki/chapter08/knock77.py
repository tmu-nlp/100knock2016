import sys
from collections import defaultdict
from knock76 import mk_label

def acc_(f):
    tp=0
    tn=0
    fp=0
    fn=0
    for line in f:
        item=mk_label(line).split("\t")
        if item[0]=="+1" and item[1]=="+1":
            tp+=1
        elif item[0]=="-1" and item[1]=="-1":
            tn+=1
        elif item[0]=="-1" and item[1]=="+1":
            fp+=1
        else:
            fn+=1
    acc=(tp+tn)/(tp+tn+fp+fn)
    pre=tp/(tp+fp)
    rec=tp/(tp+fn)
    F=2*pre*rec/(pre+rec)
    return(acc,pre,rec,F)

if __name__=="__main__":
    print(acc_(open(sys.argv[2])))
