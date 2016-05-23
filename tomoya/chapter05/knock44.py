#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk
from graphviz import Digraph

G = Digraph(format = 'png')
G.attr('node', shape = 'circle')
sentence = getChunk()
for x in sentence[:10]:
  for y in x:
    if y.dst != "-1":
        G.edge(y.morph_str(), x[int(y.dst)].morph_str())
print(G)
G.render('tree')
