#!-*-coding:utf-8-*-


num = input()
num = int(num)
list = []

for line in open("hightemp.txt", 'r'):
    line = line.strip()
    list.append(line)
list.reverse()
for line in list[:num]:
    print(line)
