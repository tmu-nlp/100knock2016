# python: python3 knock17.py ~/work/100knock_data/hightemp.txt
# UNIXコマンド: cut -f 1 ~/work/100knock_data/hightemp.txt | sort | uniq

import sys

rf = open(sys.argv[1], 'r')
ans = []

for line in rf:
    ans.append(line.split('\t')[0])
rf.close()

print('Set:', set(ans))
