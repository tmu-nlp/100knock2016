#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter = re.compile(u"{{(基礎情報)(.*)\n}}", re.DOTALL)
target = repatter.findall(f_in)
if target:
  temp = {target[0][0]: target[0][1]}
print(temp)
