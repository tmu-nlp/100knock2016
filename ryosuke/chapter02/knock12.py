with open('col1.txt', 'w') as col1f, open('col2.txt', 'w') as col2f:
    for line in open('hightemp.txt'):
        print(line.split('\t')[0], file=col1f)
        print(line.split('\t')[1], file=col2f)
# cut -f1 hightemp.txt > col1.txt
# cut -f2 hightemp.txt > col2.txt
