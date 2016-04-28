import sys

f = open("hightemp.txt")

for (i, line) in enumerate(f):
    #line = line.strip()
    line = line.split()
    if i < int(sys.argv[1]):
        print (line)

#head -n 4 hightemp.txt
