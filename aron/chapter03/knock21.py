# knock21.py
# coding: utf-8

import re
import sys
parten = re.compile(u"Category")
 
# jsonファイルを読み込む
for line in sys.stdin:
	match = parten.search(line)
	if(match):
		# newLine = line.replace(r"\n", u"\n")
		print (line)
