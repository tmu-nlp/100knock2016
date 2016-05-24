# knock33.py
import knock30

ktsList = knock30.getMorphology("neko.txt.mecab")
for item in ktsList:
	if item["pos"] == "名詞" and item["pos1"] == "サ変接続":
		print(item)