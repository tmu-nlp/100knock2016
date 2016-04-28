#!-*-coding:utf-8-*-
#split -l 5 hightemp.txt


num = int(input())
list = []
for line in open("hightemp.txt", 'r'):
    line = line.strip()
    list.append(line)
num = len(list)/num
for i,line in enumerate(list):
    line = line.strip()
    print(line)
    if i%num == num-1:
        print("\n")
