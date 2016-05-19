# knock30.py
import sys


def getMorphology(fileName):
	ketaisoLst = list()
	with open(fileName, "r") as file:
		for line in file:
			dic = dict()
			if line[0:3] == "EOS" :
				dic["surface"] = "EOS"
				dic["pos"] = "EOS"
				dic["pos1"] = "EOS"
				dic["base"] = "EOS"
			else:
				words = line.replace("\t", ",").split(",")
				dic["surface"] = words[0]
				dic["pos"] = words[1]
				dic["pos1"] = words[2]
				dic["base"] = words[7]
			ketaisoLst.append(dic)
	return ketaisoLst
	# print (dic)
def main ():
	ktsList = getMorphology("neko.txt.mecab")
	article = ""
	for kts in ktsList:
		article += kts["surface"] if kts["surface"] != "EOS" else "\n"

	print (article)
