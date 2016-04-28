#unix command "tail -n 3 hightemp.txt"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f=open("hightemp.txt","r")
s=f.read()
f.close()
print("\n".join(s.split("\n")[-1*(int(sys.argv[1])+1):]).rstrip("\n"))
