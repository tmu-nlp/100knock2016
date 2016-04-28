#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter = re.compile(u"\[\[Category:(.*)\]\]")
target = repatter.findall(f_in)
if target:
  print("\n".join(target))
