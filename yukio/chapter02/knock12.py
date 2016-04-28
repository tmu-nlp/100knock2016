-*- coding: utf-8 -*-

col1 = ""
col2 = ""
for s in open("hightemp.txt", "r"):
    words = s.split()
    col1 += words[0]
    col1 += "\n"
    col2 += words[1]
    col2 += "\n"

f = open("col1.txt", "w")
f.write(col1)
f.close()

f = open("col2.txt", "w")
f.write(col2)
f.close()
