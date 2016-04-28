#coding: utf-8
import sys
import re
f_in = open("UK.txt", "r")
repatter = re.compile(u".*Category.*")
for line in f_in:
  if repatter.search(line):
    print(line)
