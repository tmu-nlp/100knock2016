#coding: utf-8
import re
from knock20 import uktext
from collections import defaultdict

temp = re.compile("\|(.*)\s=\s(.*)")
emphasis = re.compile("'")
template = dict()
for line in uktext().split("\n"):
  line = emphasis.sub("", line)
  target = temp.search(line)
  if target:
    template[target.group(1)] = target.group(2)
for k, v in template.items():
  print("{} {}".format(k, v))
