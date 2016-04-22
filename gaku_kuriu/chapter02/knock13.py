import sys

rf1 = open(sys.argv[1], 'r')
rf2 = open(sys.argv[2], 'r')
wf = open(sys.argv[3], 'w')

column1 = rf1.readlines()
column2 = rf2.readlines()
rf1.close()
rf2.close()

for i in range(len(column1)):
    wf.write(column1[i][:-1] + '\t' + column2[i])

wf.close()
