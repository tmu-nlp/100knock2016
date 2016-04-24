# python: python3 knock10.py ~/work/100knock_data/hightemp.txt
# unixコマンド: wc ~/work/100knock_data/hightemp.txt

import sys

rf = open(sys.argv[1], 'r')
count = 0

for line in rf:
    count += 1

rf.close()
print(count)
