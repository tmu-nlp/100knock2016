#-*- coding: utf-8 -*- 

col1 = []
for s in open("hightemp.txt", "r"):
    words = s.split()
    col1.append(words[0])

print(set(col1))
