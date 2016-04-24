#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter1 = re.compile("'")
repatter2 = re.compile(u"{{(基礎情報)(.*)\n}}", re.DOTALL)
target = repatter1.sub("", f_in)
target = repatter2.findall(target)
if target:
  temp = {target[0][0]: target[0][1]}
print(temp)
