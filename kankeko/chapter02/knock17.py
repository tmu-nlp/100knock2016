#!-*-coding:utf-8-*-
#cut -f 1 hightemp.txt | sort | uniq

list = list()
set = set()
for line in open("hightemp.txt", 'r'):
    line = line.strip()
    line = line.expandtabs(1)
    list = line.split()
    set.add(list[0])

for word in set:
    print(word)
    

