# knock32.py
import knock30

ktsList = knock30.getMorphology("neko.txt.mecab")
for item in ktsList:
	if item["pos"] == "動詞":
		print(item["base"])