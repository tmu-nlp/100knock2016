# knock24.py
# coding: utf-8

import re
import sys
parten = re.compile(r"ファイル:([^¥|]*)\|")
 
# jsonファイルを読み込む
for line in sys.stdin:

	match = parten.findall(line)

	for m in match:
		# newLine = line.replace(r"\n", u"\n")
		print (m)
		# print (match.group(2))

# python3 knock20.py | python3 knock24.py