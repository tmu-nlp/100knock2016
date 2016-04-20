#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

f=open("hightemp.txt","r")
s=f.read()
f.close()
l=0
c=0
spl=""
N=int(sys.argv[1])
for line in s:
    if line=="\n":
        l+=1

if l%N==0:
    n=l/N
else:
    n=l/N+1

#splitを用いず
nc=0
for item in s:
    if item=="\n":
        c+=1
    if c==n:
        print("["+spl+"]")
        spl=""
        c=0
        nc+=1
    spl=spl+item
if nc!=N:
    print("["+spl+"]")

#splitを用いて
for i in range(N):
    spl="\n".join(s.split("\n")[i*n:(i+1)*n])
    print("["+spl+"]")
