#coding: utf-8
import re
from knock20 import uktext

repatter = re.compile(u"=+=([^=^\n]*)(==+)")
for line in uktext().split("\n"):
  target = repatter.search(line)
  if target:
    print(target.group(1), len(target.group(2)) - 1)
