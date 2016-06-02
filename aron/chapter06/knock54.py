# knock54.py
# coding = utf-8

import sys
import xml.etree.ElementTree as ET
# def pareXml(input):
# 	for line in input:
# 		line = line.strip()
# 		re.match(line, "<\s\W.*>")
# 	

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

tokens = root.findall(".//token")
for token in tokens:

	word = token.find("word").text
	lemma = token.find("lemma").text
	pos = token.find("POS").text
	print ("%s\t%s\t%s" % (word, lemma, pos))