# knock34.py
# -*- coding: utf-8 -*-

import knock30

ktsList = knock30.getMorphology("neko.txt.mecab")
for i in range(len(ktsList) - 2):
	if(ktsList[i]["pos"] == u"名詞" and ktsList[i + 1]["surface"]== "の" and ktsList[i + 2]["pos"] == u"名詞"):
		print (ktsList[i]["surface"] + ktsList[i + 1]["surface"] + ktsList[i + 2]["surface"])
