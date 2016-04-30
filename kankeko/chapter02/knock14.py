#!-*-coding:utf-8-*-
#head -n N hightemp.txt


num = input()
num = int(num)

for i,line in enumerate(open("hightemp.txt", 'r')):
    if i < num:
        line = line.strip()
        print(line)
