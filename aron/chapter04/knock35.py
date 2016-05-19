# knock35.py
# -*- coding: utf-8 -*-

import knock30

ktsList = knock30.getMorphology("neko.txt.mecab")

nounList = list()
for item in ktsList:
	if(item["pos"] == "名詞"):
		nounList.append(item["surface"])
	else:
		if(len(nounList) > 1):
			print ("".join(nounList), ":", len(nounList))
		nounList.clear()
