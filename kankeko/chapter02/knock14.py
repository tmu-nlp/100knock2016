#!-*-coding:utf-8-*-


num = input()
num = int(num)

for i,line in enumerate(open("hightemp.txt", 'r')):
    if i < num:
        line = line.strip()
        print(line)
