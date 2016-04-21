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
    
