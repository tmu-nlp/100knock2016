# knock53.py
# coding = utf-8
# http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip

import sys
import xml.etree.ElementTree as ET
# def pareXml(input):
# 	for line in input:
# 		line = line.strip()
# 		re.match(line, "<\s\W.*>")
# 	

tree = ET.parse("nlp.txt.xml")
root = tree.getroot()

eleList = root.findall(".//word")
for e in eleList:
	print(e.text);