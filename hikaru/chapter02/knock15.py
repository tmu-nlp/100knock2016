import sys
f = open("hightemp.txt")
f2 = open("hightemp.txt")
for (i, line) in enumerate(f):
    line = line.split()
#print (i)
for (j, line2) in enumerate(f2):
    line2 = line2.split()
    if j > (i - int(sys.argv[1])): #argv=4 20 > 23 - 4
        print (line2)

# tail -n 4 hightemp.txt
