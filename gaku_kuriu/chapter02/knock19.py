# python: python3 knock19.py ~/work/100knock_data/hightemp.txt
# UNIXコマンド: cut -f 1 ~/work/100knock_data/hightemp.txt | sort | uniq -c | sort -r

import sys
from collections import defaultdict

rf = open(sys.argv[1], 'r')
freqdict = defaultdict(int)

for line in rf:
    freqdict[line.split('\t')[0]] += 1
rf.close()

for k, v in sorted(freqdict.items(), key=lambda x:x[1], reverse=True):
    print(v, k)
