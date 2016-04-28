import sys

l = [None] * int(sys.argv[1])
for line in open('hightemp.txt'):
    l.pop(0)
    l.append(line.rstrip('\n'))
for line in l:
    print(line)

# tail -n4 hightemp.txt
