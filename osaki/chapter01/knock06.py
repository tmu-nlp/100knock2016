def bigram(s):
    ans=[]
    t=""
    for i in range(len(s)-1):
        t=s[i]+s[i+1]
        ans=ans+[t]
        t=""
    return ans

def clear(x):
    c1=0
    for i in x:
        c1+=1
        xc=x[c1:]
        c2=c1
        for j in xc:
            if i==j:
                del x[c2]
                c2-=1
            c2+=1
    return x

a="paraparaparadise"
b="paragraph"
pro=[]
x=clear(bigram(a))
y=clear(bigram(b))
sum=clear(x+y)
for i in x:
    c=0
    for j in y:
        if i==j:
            pro=pro+[i]
            c+=1
dif=sum-pro
print(sum)
print(dif)
print(pro)
