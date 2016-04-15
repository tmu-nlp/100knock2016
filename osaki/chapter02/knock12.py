f0=open("hightemp.txt","r")
s=f0.read()
col=[]
f0.close()
for i in s.split("\n"):
    col=col+[i]
f1=open("col1.txt","w")
f2=open("col2.txt","w")
f1.write(col[0])
f2.write(col[1])
f1.close()
f2.close()
