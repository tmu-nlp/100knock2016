# python: python3 knock18.py ~/work/100knock_data/hightemp.txt
# UNIXコマンド: sort -k3r ~/work/100knock_data/hightemp.txt

import sys

rf = open(sys.argv[1], 'r')
ans = []

for line in rf:
    ans.append((line.split('\t')[2], line))
rf.close()

for k, v in sorted(ans, reverse=True):
    print(v, end="")
    
