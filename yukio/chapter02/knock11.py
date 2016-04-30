# -*- coding: utf-8 -*-

ans = ""
for s in open("hightemp.txt", "r"):
    s = s.replace("\t", " ")
    ans += s
print(ans)

# expand hightemp.txt
