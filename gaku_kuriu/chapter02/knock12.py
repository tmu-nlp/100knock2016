# python: python3 knock12.py ~/work/100knock_data/hightemp.txt ~/work/100knock_data/col1.txt ~/work/100knock_data/col2.txt
# UNIXコマンド: cut -f 1 ~/work/100knock_data/hightemp.txt , cut -f 2 ~/work/100knock_data/hightemp.txt

import sys

rf = open(sys.argv[1], 'r')
wf1 = open(sys.argv[2], 'w')
wf2 = open(sys.argv[3], 'w')

for line in rf:
    wf1.write(line.split('\t')[0]+'\n')
    wf2.write(line.split('\t')[1]+'\n')

rf.close()
wf1.close()
wf2.close()
