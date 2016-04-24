#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter1 = re.compile("'")
repatter2 = re.compile(r"\[\[([^:]*?)\]\]")
repatter3 = re.compile(u"{{(基礎情報)(.*)\n}}", re.DOTALL)
target = repatter1.sub(u"", f_in)
target = repatter2.sub(r"\1", target)
target = repatter3.findall(target)
print(target)
if target:
  temp = {target[0][0]: target[0][1]}
  print(temp)
