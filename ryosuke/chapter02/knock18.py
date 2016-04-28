lines = open('hightemp.txt').readlines()
for line in sorted(lines, key= lambda x: x.split('\t')[2], reverse=True):
    print(line.rstrip('\n'))

# sort -k 3 -r hightemp.txt
