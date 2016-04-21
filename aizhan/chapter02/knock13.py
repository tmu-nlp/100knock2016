col1 = open('col1.txt').read().split('\n')
col2 = open('col2.txt').read().split('\n')
col1tabcol2 = open('col1tabcol2','w')

for (x,y) in zip(col1,col2):
    col1tabcol2.write(x + '\t' + y + '\n')

