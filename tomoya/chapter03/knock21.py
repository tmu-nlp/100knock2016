#coding: utf-8
from knock20 import uktext
import re
repatter = re.compile(u".*Category.*")
for line in uktext().split("\n"):
  if repatter.search(line):
    print(line)
