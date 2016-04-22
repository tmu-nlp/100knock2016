import sys

rf = open(sys.argv[1], 'r')
ans = []

for line in rf:
    ans.append((line.split('\t')[2], line))
rf.close()

for k, v in sorted(ans, reverse=True):
    print(v, end="")
    
