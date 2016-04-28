# -*- coding: utf-8 -*-

import sys
i = 0
for s in open("hightemp.txt", "r"):
    s = s.strip()
    if i < int(sys.argv[1]):
        print(s)
        i += 1
    else:
        break 

# head -n 5 hightemp.txt 
