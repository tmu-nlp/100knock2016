import sys

rf = open(sys.argv[1], 'r')

for line in rf:
    print(line.replace('\t', ' '), end='')

rf.close()
