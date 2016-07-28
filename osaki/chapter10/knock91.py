flag=0
f=open("knock91.txt","w")
for line in open("questions-words.txt","r"):
    if flag==0 and line==": family\n":
        flag=1
    elif flag==1 and line[0]==":":
        flag=-1
    elif flag==-1:
        break
    elif flag==1:
        f.write(line)
f.close
