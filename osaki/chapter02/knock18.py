s=[]
for line in open("hightemp.txt"):
    s=s+[line.split()]
t=sorted(s,key=lambda x:x[2])
for item in t:
    print "\t".join(item)
