#-*- coding: utf-8 -*-

read = open("hightemp.txt", "r")
ans = []

for lines in read:
    lines = lines.strip()
    word = lines.split()
    if word[0] not in ans:
        ans.append(word[0])

for i in range(len(ans)):
    print ans[i]

 
