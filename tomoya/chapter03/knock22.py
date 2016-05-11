#coding: utf-8
import re
from knock20 import uktext
repatter = re.compile(u"\[\[Category:(.*)\]\]")
for line in uktext().split("\n"):
  target = repatter.search(line)
  if target != None:
    print(target.group(1))
