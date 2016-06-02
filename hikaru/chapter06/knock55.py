from knock50 import getsentence
import re
from xml.etree import ElementTree

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()
wordlist = root.findall('.//word')
NERlist = root.findall('.//NER')
for word, NER in zip(wordlist, NERlist):
    if NER.text == 'PERSON':
        print (word.text)