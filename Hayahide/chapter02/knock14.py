#-*- coding: utf-8 -*-
read = open("hightemp.txt", "r")
N = int(raw_input())
count = 0

while count < N:
    print (read.readline()).rstrip()
    count += 1

read.close()

#UNIX command: head -n 3 hightemp.txt
#高知県  江川崎  41  2013-08-12
#埼玉県  熊谷    40.9    2007-08-16
#岐阜県  多治見  40.9    2007-08-16

