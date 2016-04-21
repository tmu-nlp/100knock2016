#!-*-coding:utf-8-*-

list = list()
set = set()
for line in open("hightemp.txt", 'r'):
    line = line.strip()
    line = line.expandtabs(1)
    list = line.split()
    set.add(list[0])

for word in set:
    print(word)
    

