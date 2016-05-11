#coding: utf-8
import re
from knock20 import uktext

temp = re.compile("\|(.*)\s=\s(.*)")
template = dict()
for line in uktext().split("\n"):
  target = temp.search(line)
  if target:
    template[target.group(1)] = target.group(2)
print(template)
