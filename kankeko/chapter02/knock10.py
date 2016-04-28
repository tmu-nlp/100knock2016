#!-*-coding:utf-8-*-
#wc hightemp.txt


import sys


f = open("hightemp.txt")
lines2 = f.readlines()
f.close()

for i,line in enumerate(lines2):
    print line
print i+1


