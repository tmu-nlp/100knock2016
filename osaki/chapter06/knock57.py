import sys
from xml.etree.ElementTree import *

tree=parse(sys.argv[1])
elem=tree.getroot()

result="digraph{\n"
c=0
for e in elem.getiterator():
    if e.tag=="governor":
        result+='\t"'+e.text+'" -> '
    elif e.tag=="dependent":
        result+='"'+e.text+'";\n'
    elif e.tag=="dependencies":
        c+=1
        if c==int(sys.argv[2])*2:
            result+="}"
            break
        result="digraph{\n"

f=open("knock57.dot","w")
f.write(result)
f.close
