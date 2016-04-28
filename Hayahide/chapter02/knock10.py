#-*- coding: utf-8 -*-

f = open("hightemp.txt", "r")
count = 0

for i in f:
    count += 1

print count

#UNIX command: wc -l hightemp.txt
