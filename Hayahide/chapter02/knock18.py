#-*- coding: utf-8 -*-

read = open("hightemp.txt", "r")

ans = []

for line in read:
    line = line.strip()
    word = line.split()
    ans.append(word)

for i in sorted(ans, key = lambda x:x[2], reverse = True):
    print "\t".join(i)
