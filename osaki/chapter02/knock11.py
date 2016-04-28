#unix command "expand -t 1 hightemp.txt"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

f1=open("hightemp.txt","r")
s=f1.read()
f1.close()
s=s.replace("	"," ")
f2=open("new.txt","w")
f2.write(s)
f2.close()
