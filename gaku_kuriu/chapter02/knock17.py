import sys

rf = open(sys.argv[1], 'r')
ans = []

for line in rf:
    ans.append(line.split('\t')[0])
rf.close()

print('Set:', set(ans))
