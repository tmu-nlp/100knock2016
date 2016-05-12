#coding: utf-8
import re
from knock20 import uktext
from collections import defaultdict

temp = re.compile("\|(.*)\s=\s(.*)")
emphasis = re.compile("'|<.*>")
internallink = re.compile(r"\[\[(ファイル:)*(.*?)\]\]")
others = re.compile(r"\*")
template = dict()
for line in uktext().split("\n"):
  line = emphasis.sub("", line)
  line = internallink.sub(r"\2", line)
  line = others.sub(" ", line)
  target = temp.search(line)
  if target:
    template[target.group(1)] = target.group(2)
for k, v in sorted(template.items(), key=lambda x: x[0]):
  print("{} {}".format(k, v))

