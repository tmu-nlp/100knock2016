#unix command "cut -f 1 < hightemp.txt | sort | uniq -c | sort -r"

f=open("col1.txt","r")
s=f.read()
f.close()
d=dict()
t1=[]
t2=[]
for i in s.split("\n"):
    if d.has_key(i)==False:
        d[i]=0
    else:
       d[i]=str(int(d[i])+1)
for i in d.keys():
    t1=t1+[[i,d[i]]]
t2=sorted(t1,key=lambda x:x[1])
t2.reverse()
for i in t2:
    print i[0]
