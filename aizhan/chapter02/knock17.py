#cut -f 1 hightemp.txt | sort | uniq

hightemp = open('hightemp.txt').readlines()
newline = []

for line in hightemp:
    newl = line.split('\t')
    newline.append(newl[0])

newset = set(newline)

print(newset)

