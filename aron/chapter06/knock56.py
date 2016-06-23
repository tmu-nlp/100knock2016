# knock56.py
# coding = utf-8

import sys
import xml.etree.ElementTree as ET

            # <NER>PERSON</NER>
tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

sentenceNodes = root.findall(".//sentences/sentence")
sentList =[]

print (len(sentenceNodes))
print ("==========================")

for i, sent in enumerate(sentenceNodes):
	words = []

	tokens = sent.findall(".//token")

	for token in tokens:
		# ner = token.find("NER").text
		# if(ner == "PERSON"):
		# wordNodes = token.find("word").text
		words.append(token.find("word").text)
	sentList.append(words)
lineNo =0 
for sent in sentList:
	print(lineNo, " ".join(sent))
	lineNo +=1


print ("==========================")

referList = []
referNodes = root.findall(".//coreference")

# <mention>
# 	<sentence>18</sentence>
# 	<start>23</start>
# 	<end>25</end>
# 	<head>24</head>
# 	<text>language processing</text>
# </mention>

for ref in referNodes:
	mentList = ref.findall(".//mention")
	representative = mentList[0].find("text").text
	representList = representative.split()
	representList.insert(0, "(")
	representList.append("|")
	for ment in mentList[1:]:
		senId = int(ment.find("sentence").text) - 1
		start = int(ment.find("start").text) -1
		end   = int(ment.find("end").text)-1

		sentence = sentList[senId]

		# sentence.insert(start, "")
		sentence.insert(end, ")")
		# http://www.karak.jp/blog/python-list.html
		sentence[start:start] = representList


lineNo =0 
for sent in sentList:
	print(lineNo, " ".join(sent))
	lineNo +=1


















