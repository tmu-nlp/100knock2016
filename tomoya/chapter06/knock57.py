#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
from graphviz import Digraph
search_governor = re.compile('<governor idx="([0-9]*?)".*>(.*)</governor>')
search_dependent = re.compile('<dependent idx="([0-9]*?)".*>(.*)</dependent>')
G = Digraph(format = 'png')
G.attr('node', shape = 'circle')
flag = False
sentence = 0
for line in open("nlp.txt.out"):
  if '<dependencies type="collapsed-dependencies">' in line:
    flag = True 
  elif flag == True and "</dependencies>" in line:
     flag = False
  if flag:
    governor = search_governor.search(line)
    dependent = search_dependent.search(line)
    if governor:
      if governor.group(2) == "ROOT":
        sentence += 1
        if sentence > 4:
          break
      gov = str(sentence) + "-" + governor.group(1) 
      G.node(gov, governor.group(2))
    elif dependent:
      dep = str(sentence) + "-" + dependent.group(1)
      G.node(dep, dependent.group(2))

      G.edge(gov, dep)
G.render('tree')


