from xml.etree.ElementTree import *
import sys

tree=parse(sys.argv[1])
elem=tree.getroot()

result=""
for e in elem.getiterator():
    if e.tag=="word" or e.tag=="lemma":
        result+=e.text+"\t"
    elif e.tag=="POS":
        result+=e.text+"\n"

print(result)
