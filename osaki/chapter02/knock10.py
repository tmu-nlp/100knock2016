#!/usr/bin/env python
# -*- coding: utf-8 -*-

f=open("hightemp.txt","r")
s=f.read()
f.close()
l=0
for line in s:
    if line=="\n":
        l+=1

print(l)
