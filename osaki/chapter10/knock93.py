c=0
t=0

for (line1,line2) in zip(open("knock92.txt","r"),open("knock91.txt","r")):
    c+=1
    if line1==line2:
        t+=1

print(str(t*100/c)+"%")
