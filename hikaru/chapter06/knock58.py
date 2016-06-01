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
                SV_list.append((V1, S))

            if dep.get("type") == 'dobj':
                V2 = dep.find('.//governor').text
                O = dep.find('.//dependent').text
                VO_list.append((V2, O))
        SVO_dict = defaultdict(list)
        for key, value in SV_list:
            SVO_dict[key].append(value)
        #for key, value in SVO_dict:
            #if len(value) > 1:
                #SVO_dict[key] = [' '.join(value)]
        print (SVO_dict)
        for key, value in VO_list:
            SVO_dict[key].append(value)
        print (SVO_dict)
