# python: python3 knock15.py 任意の数N ~/work/100knock_data/hightemp.txt
# UNIXコマンド: tail -n 任意の数N ~/work/100knock_data/hightemp.txt

import sys

N = int(sys.argv[1])
rf = open(sys.argv[2], 'r')

lines = rf.readlines()
rf.close()

for line in lines[-N:]:
    print(line, end="")
