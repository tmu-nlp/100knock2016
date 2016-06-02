import sys
from xml.etree.ElementTree import *

tree=parse(sys.argv[1])
elem=tree.getroot()

for e in elem.findall(".//word"):
    print(e.text)
