# -*- coding: utf-8 -*-

ans = ""
for col1, col2 in zip(open("col1.txt", "r"), open("col2.txt", "r")):
    col1 = col1.strip()
    col2 = col2.strip()
    ans = ans + "\t".join([col1, col2]) + "\n"

f = open("merge.txt", "w")
f.write(ans)
f.close()

#paste col1.txt col2.txt
