#!-*-coding:utf-8-*-
#cut -f 1 hightemp.txt | sort | uniq -c | sort -nr

from collections import defaultdict


dict = defaultdict(lambda: 0)
list = []
list1 = []
for line in open("hightemp.txt", 'r'):
    line = line.strip()
    line = line.expandtabs(1)
    list = line.split()
    list1.append(list[0])
for word in list1:
        dict[word] += 1
for name,count in reversed(sorted(dict.items(),key=lambda x:x[1])):
    print(name)
