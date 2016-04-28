cut -f 1,2 hightemp.txt

hightemp = open('hightemp.txt')
col1 = open('col1.txt','w')
col2 = open('col2.txt','w')
newline = []
tab2 = 0

for line in hightemp:
    newline = line.split('\t')
    col1.write(newline[0]+'\n')
    col2.write(newline[1]+'\n')
            
col1.close()
col2.close()
