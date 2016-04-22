import sys

N = int(sys.argv[1])
rf = open(sys.argv[2], 'r')

lines = rf.readlines()
rf.close()

for line in lines[:N]:
    print(line, end="")

