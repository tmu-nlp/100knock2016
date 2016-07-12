import sys

del_list=[".",",","!","?",";",":","(",")","[","]","'",'"']
with open("knock80.txt","w") as f:
    for line in open(sys.argv[1]):
        tokens=[]
        for token in line.strip("\n").split(" "):
            flag=True
            while flag==True:
                flag=False
                if token != "":
                    if token[0] in del_list:
                        token=token[1:]
                        flag=True
                if token != "":
                    if token[-1] in del_list:
                        token=token[:-1]
                        flag=True
            if token != "":
                tokens+=[token]
        if tokens!=[]:
            f.write(" ".join(tokens)+"\n")
