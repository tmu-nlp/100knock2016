import sys

rf = open(sys.argv[1], 'r')
count = 0

for line in rf:
    count += 1

rf.close()
print(count)
