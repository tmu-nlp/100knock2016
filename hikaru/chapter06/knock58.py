from knock50 import getsentence
import re
from xml.etree import ElementTree
from collections import defaultdict

XMLFILE = "nlp.txt.out"
tree = ElementTree.parse(XMLFILE)
root = tree.getroot()

dependencieslist = root.findall('.//dependencies')
for dependencies in dependencieslist:
    if dependencies.get("type") == 'collapsed-ccprocessed-dependencies':
        deplist = dependencies.findall('.//dep')
        SV_list = list()
        VO_list = list()
        for dep in deplist:
            if dep.get("type") == 'nsubj':
                V1 = dep.find('.//governor').text
                S = dep.find('.//dependent').text
                idx = dep.find('.//governor').get("idx")
                SV_list.append(('{0} {1}'.format(V1, idx), S))

            if dep.get("type") == 'dobj':
                V2 = dep.find('.//governor').text
                O = dep.find('.//dependent').text
                idx = dep.find('.//governor').get("idx")
                VO_list.append(('{0} {1}'.format(V2, idx), O))
        SVO_dict = defaultdict(list)
        for key, value in SV_list:
            SVO_dict[key].append(value)
        for key, value in VO_list:
            SVO_dict[key].append(value)
        #print (SVO_dict)
        for key, value in SVO_dict.items():
            if len(value) > 1:
                print (value[0] + '\t' + key.split()[0] + '\t' + value[1])

