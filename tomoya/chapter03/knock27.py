#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter1 = re.compile(u"{{基礎情報\s([^\n]*)\n(.*)\n}}", re.DOTALL)
repatter2 = re.compile("'")
repatter3 = re.compile(r"\[\[([^:]*?)\]\]")
target = repatter1.findall(f_in)
if target:
  temp = {target[0][0]: target[0][1]}
target = repatter2.sub("", temp["国"])
target = repatter3.sub(r"\1", target)
print(target)

