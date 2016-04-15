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
dif=[]
x=clear(bigram(a))
if "se" in x:
    print("x has se")
y=clear(bigram(b))
if "se" in y:
    print("y has se")
sum=clear(x+y)
for i in x:
    for j in y:
        if i==j:
            pro=pro+[i]
dif=clear(x+y)
for i in pro:
    c=0
    for j in dif:
        if i==j:
            del dif[c]
        c+=1
print(sum)
print(dif)
print(pro)
