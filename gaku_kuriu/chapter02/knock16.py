# python: python3 knock16.py 任意の分割数N ~/work/100knock_data/hightemp.txt ~/work/100knock_data/knock16/hightemp
# UNIXコマンド: split -l 任意の分割数N ~/work/100knock_data/hightemp.txt ~/work/100knock_data/knock16/hightemp_unix

import sys

N = int(sys.argv[1])
rf = open(sys.argv[2], 'r')
wfname = sys.argv[3]

lines = rf.readlines()
rf.close()

splitlines = [lines[i:i+(len(lines)//N)] for i in range(0, len(lines), len(lines)//N)]
for i in range(len(splitlines)):
    if i == (N-1):
        wf = open(wfname+'_'+str(i)+'.txt', 'w')        
        for line in [l for sl in splitlines[i:] for l in sl]:
            wf.write(line)
        wf.close()
        break
    else:
        wf = open(wfname+'_'+str(i)+'.txt', 'w')
        for line in splitlines[i]:
            wf.write(line)
        wf.close()
    
