import sys

d={}

for line in open(sys.argv[1]):
    d[line.split("\t")[0]]=float(line.strip("\n").split("\t")[1])

c=0
for key,value in sorted(d.items(),key=lambda x:x[1],reverse=True):
    c+=1
    print(key+"\t"+str(value))
    if c==10:
        break

c=0
for key,value in sorted(d.items(),key=lambda x:x[1]):
    c+=1
    print(key+"\t"+str(value))
    if c==10:
        break
