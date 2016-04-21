import sys
from collections import defaultdict

hightemp = open('hightemp.txt')
words = defaultdict(lambda:0)
newline = []

for line in hightemp:
    line = line.strip().split()
    newline.append(line[0])

for word in newline:
    words[word] += 1

for key, value in sorted(words.items()):
    print(str(key) + ' ' + str(value))

