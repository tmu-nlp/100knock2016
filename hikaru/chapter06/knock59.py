from knock50 import getsentence
import re
from xml.etree import ElementTree
from nltk.tree import Tree

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()
parselist = root.findall('.//parse')
#s_parse = re.compile('(?P<NP>\(NP.*)')
for parse in parselist:
    tree = Tree.fromstring(parse.text)
    for NP in tree.subtrees(lambda x: x.label() == 'NP'):
        print (NP)