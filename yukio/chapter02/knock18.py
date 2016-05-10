#*- coding: utf-8 -*- 

d = []
for s in open("hightemp.txt", "r"):
    words = s.split()
    d.append(words)
ans = sorted(d, key = lambda x: x[2], reverse = True)

for s in ans:
    print("\t".join(s))
