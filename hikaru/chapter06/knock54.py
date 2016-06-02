from knock50 import getsentence
import re
from xml.etree import ElementTree

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()
wordlist = root.findall('.//word')
lemmalist = root.findall('.//lemma')
POSlist = root.findall('.//POS')
for word, lemma, POS in zip(wordlist, lemmalist, POSlist):
    print (word.text + '\t' + lemma.text + '\t' + POS.text)