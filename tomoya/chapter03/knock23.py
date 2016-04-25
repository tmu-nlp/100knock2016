#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r")
repatter = re.compile(u"=+=([^=^\n]*)(==+)")
for line in f_in:
  target = repatter.search(line)
  if target:
    level = len(target.group(2)) - 1
    print(target.group(1), level)
