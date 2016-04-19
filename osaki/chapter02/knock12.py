#!/usr/bin/env python
# -*- coding: utf-8 -*-

col1=""
col2=""

for i in open("hightemp.txt"):
    col1=col1+i.strip().split("\t")[0]+"\n"
    col2=col2+i.strip().split("\t")[1]+"\n"
f1=open("col1.txt","w")
f2=open("col2.txt","w")
f1.write(col1)
f2.write(col2)
f1.close()
f2.close()
