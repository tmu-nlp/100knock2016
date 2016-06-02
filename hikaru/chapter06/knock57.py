from graphviz import Digraph
from knock50 import getsentence
import re
from xml.etree import ElementTree

dot = Digraph(format = 'png')
XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()

count = 0
i = 0
dependencieslist = root.findall('.//dependencies')
for dependencies in dependencieslist:
    if dependencies.get("type") == 'collapsed-ccprocessed-dependencies':
        deplist = dependencies.findall('.//dep')
        for dep in deplist:
            governor = dep.find('.//governor')
            dependent = dep.find('.//dependent')
            governor_idx = int(governor.get("idx"))
            dependent_idx = int(dependent.get("idx"))
            #print (governor.text)
            #print (dependent.text)
            #print (governor_idx, dependent_idx)
            dot.node('{0}-{1}'.format(governor_idx, i), governor.text)
            dot.node('{0}-{1}'.format(dependent_idx, i), dependent.text)
            dot.edge('{0}-{1}'.format(governor_idx, i), '{0}-{1}'.format(dependent_idx, i))
        count += 1
        i += 1
    if count == 3:
        break

dot.render('tree')
