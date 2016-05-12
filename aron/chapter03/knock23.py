# knock23.py
# coding: utf-8

import re
import sys
parten = re.compile(r"(={2,})([^{= }]+)={2,}")
 
# jsonファイルを読み込む
for line in sys.stdin:
	# jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
	# data = json.load(f)
	# ファイルを閉じる
	# f.close()

	match = parten.search(line)
	if(match):
		# newLine = line.replace(r"\n", u"\n")
		print ("%s, %s, level:%d" % (match.group(0), match.group(2), len(match.group(1)) - 1 ))
		# print (match.group(2))

		
# python3 knock20.py | python3 knock23.py