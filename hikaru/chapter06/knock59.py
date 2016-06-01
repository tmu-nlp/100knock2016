from knock50 import getsentence
import re
from xml.etree import ElementTree

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()
parselist = root.findall('.//parse')
#s_parse = re.compile('(?P<NP>\(NP.*)')
for parse in parselist:
    print (parse.text)