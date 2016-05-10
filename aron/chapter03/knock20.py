# knock20.py
# coding: utf-8

import re
parten = re.compile(u"\"イギリス\"")
 
# jsonファイルを読み込む
with open("jawiki-country.json") as f:
	# jsonデータを読み込んだファイルオブジェクトからPythonデータを作成
	# data = json.load(f)
	# ファイルを閉じる
	# f.close()

	for line in f:
		match = parten.search(line)
		if(match):
			# newLine = line.replace(r"\n", u"\n")
			print (line)

# 普通に表示
# print("普通に表示")
# print(data)