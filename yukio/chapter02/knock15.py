# -*- coding: utf-8 -*-

import sys

ans = []
i = 0 
for s in open("hightemp.txt", "r"):
    s = s.strip()
    ans.append(s)
    i += 1

for j in range(i - int(sys.argv[1]), i):
    print(ans[j])

# tail -n 5 hightemp.txt 
