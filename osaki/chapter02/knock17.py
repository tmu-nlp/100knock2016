#unix command "cut -f 1 < hightemp.txt | sort | uniq"

f=open("col1.txt","r")
s=f.read()
f.close()
d=dict()
for i in s.split("\n"):
    d[i]=0
for key in d.keys():
    print key
