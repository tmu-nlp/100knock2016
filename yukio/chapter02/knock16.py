# -*- coding: utf-8 -*-

import sys

d = []
i = 0
for s in open("hightemp.txt", "r"):
    d.append(s)
    i += 1

n = []
for j in range(0, int(sys.argv[1])):
    n.append(int(i / int(sys.argv[1])))

for j in range(0, i % int(sys.argv[1])):
    n[j] += 1

count = 0

for j in range(0, int(sys.argv[1])):
    ans = ""
    for k in range(0, n[j]):
        ans = ans + d[count] + "\n"
        count += 1

    fn = "split" + str(j + 1) + ".txt"
    f = open(fn, "w")
    f.write(ans)
    f.close()
