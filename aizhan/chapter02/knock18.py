#sort -rk3 hightemp.txt

from operator import itemgetter
hightemp = open('hightemp.txt')
lines = []

for line in hightemp:
    lines.append(line.split())

lines.sort(key=itemgetter(2),reverse=True)

for line in lines:
    print('\t'.join(line))

