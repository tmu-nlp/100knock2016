import sys
import random

with open("knock82.txt","w") as f:
    for line in open(sys.argv[1]):
        tokens=line.strip("\n").split(" ")
        for i in range(len(tokens)):
            d=random.randint(1,5)
            c_list=tokens[max(i-d,0):i]+tokens[i+1:i+d+1]
            for c in c_list:
                f.write(tokens[i]+"\t"+c+"\n")
