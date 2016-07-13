import sys

c_list=list()
for line in open(sys.argv[2]): #国名リストの読み込み
    c_list+=[line.strip("\n")]

with open("knock81.txt","w") as f:
    for line in open(sys.argv[1]):
        line=line.strip("\n")
        for item in c_list:
            item_r=item.replace(" ","_")
            line=line.replace(item,item_r)
        f.write(line+"\n")
