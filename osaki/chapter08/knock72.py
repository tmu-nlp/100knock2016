from nltk import stem
from nltk.corpus import stopwords
from collections import defaultdict

def mk_feature():
    d=defaultdict(lambda:0)
    stoplist=stopwords.words("english")+[",",".","!","?",";",":","\n","\t","(",")"," ",""]
    stemmer=stem.PorterStemmer()
    l=list()

    for line in open("sentiment.txt","r"):
        y=line.split(" ")[0]
        for item in line.strip("\n").split(" ")[1:]:
            item=stemmer.stem(item)
            if item not in stoplist:
                d[item]+=1
    for key,value in d.items():
        if value < 5:
            l+=[key]
    for key in l:
        del d[key]
    return(d)

if __name__=="__main__":
    d=mk_feature()
    for key,value in d.items():
        print(key+"\t"+str(value))
