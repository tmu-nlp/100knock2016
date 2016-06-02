import re
from graphviz import Digraph


search_governor = re.compile('<governor idx="(?P<gov_idx>[0-9]*?)".*>(?P<governor>.*)</governor>')
search_dependent = re.compile('<dependent idx="(?P<dep_idx>[0-9]*?)".*>(?P<dependent>.*)</dependent>')
G = Digraph(format='png')
G.attr('node', shape='circle')
flag = False
sentence = 0
for line in open("nlp.txt.out"):
    if '<dependencies type="collapsed-dependencies">' in line:
        flag = True
    elif flag and "</dependencies>" in line:
        flag = False
    if flag:
        governor = search_governor.search(line)
        dependent = search_dependent.search(line)
        if governor:
            if governor.group("governor") == "ROOT":
                sentence += 1
            if sentence > 3:
                break
            gov = str(sentence) + "-" + governor.group("gov_idx")
            G.node(gov, governor.group("governor"))
        elif dependent:
            dep = str(sentence) + "-" + dependent.group("dep_idx")
            G.node(dep, dependent.group("dependent"))
            G.edge(gov, dep)
G.render('tree')
