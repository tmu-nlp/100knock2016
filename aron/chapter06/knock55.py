# knock55.py
# coding = utf-8

import sys
import xml.etree.ElementTree as ET

            # <NER>PERSON</NER>
tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

tokens = root.findall(".//token")
for token in tokens:
	ner = token.find("NER").text
	if(ner == "PERSON"):
		word = token.find("word").text
		print ("%s" % (word))