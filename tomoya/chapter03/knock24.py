#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r").read()
repatter = re.compile(u"ファイル:(.*(?:.svg|\.jpg|\.JPG))")
target = repatter.findall(f_in)
if target:
  print("\n".join(target))
