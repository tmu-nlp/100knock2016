from xml.etree.ElementTree import *
import sys

tree=parse(sys.argv[1])
elem=tree.getroot()

result=""
word=""
for e in elem.getiterator():
    if e.tag=="word":
        word=e.text
    if e.tag=="NER" and e.text=="PERSON":
        result+=word+"\n"

print(result.strip("\n"))
