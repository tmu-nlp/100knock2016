#unix command "head -n N hightemp.txt"

import sys

f=open("hightemp.txt","r")
s=f.read()
f.close()
c=0
for i in s.split("\n"):
    print(i)
    c+=1
    if c == int(sys.argv[1]):
        break
