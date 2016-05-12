# knock21.py
# coding: utf-8

import json
import re
import sys
parten = re.compile(r"\[\[Category:(.*)\]\]")
 
# jsonファイルを読み込む
for line in sys.stdin:

	match = parten.search(line)
	if(match):
		# newLine = line.replace(r"\n", u"\n")
		print (match.group(1))

		
# python3 knock20.py | python3 knock21.py | python3 knock22.py