# python: python3 knock11.py ~/work/100knock_data/hightemp.txt
# UNIXコマンド: cat ~/work/100knock_data/hightemp.txt | sed $'s/\t/ /g'

import sys

rf = open(sys.argv[1], 'r')

for line in rf:
    print(line.replace('\t', ' '), end='')

rf.close()
