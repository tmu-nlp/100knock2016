f1=open("col1.txt","r")
s1=f1.read()
f1.close()
f2=open("col2.txt","r")
s2=f2.read()
f2.close()
c=0
s0=""
for i in s1.split("\n"):
    s0=s0+s1.split("\n")[c]+"	"+s2.split("\n")[c]+"\n"
    c+=1
f0=open("col.txt","w")
f0.write(s0)
f0.close()
