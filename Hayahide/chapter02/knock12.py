#-*- coding: utf-8 -*-

r = open("hightemp.txt", "r")

column1 = ""
column2 = ""

for line in r:
    temp = line.split()
    column1 = column1 + temp[0] + "\n"
    column2 = column2 + temp[1] + "\n"

w = open("col1.txt", "w")
w.write(column1)
w.close()
w = open("col2.txt", "w")
w.write(column2)
w.close()

#UNIX command: cut -f 1 hightemp.txt > col1_unix.txt
#              cut -f 2 hightemp.txt > col2_unix.txt
