#!-*-coding:utf-8-*-
#expand -t 1 hightemp.txt


for line in open("hightemp.txt"):
    line = line.strip()
    print(line.expandtabs(1))
