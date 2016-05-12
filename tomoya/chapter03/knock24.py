#coding: utf-8
import re
from knock20 import uktext

repatter = re.compile(u"ファイル:(.*(?:.svg|\.jpg|\.JPG))")
for line in uktext().split("\n"):
  target = repatter.search(line)
  if target:
    print(target.group(1))
