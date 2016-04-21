def ngram(s,x):
    bigram=[]
    t=""
    for i in range(len(s)-x+1):
        for j in range(x):
            t=t+s[i+j]
        bigram=bigram+[t]
        t=""
    print(bigram)

ngram("I am an NLPer",2)
ngram(["I","am","an","NLPer"],2)
