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
for id1, x in enumerate(sentence[:10]):
  for id2, y in enumerate(x):
    if y.dst != "-1":
        G.node(str(id1) + str(id2), y.morph_str("surface"))
        G.node(str(id1) + y.dst, x[int(y.dst)].morph_str("surface"))
        G.edge(str(id1) + str(id2), str(id1) + y.dst)
        print(G)
G.render('tree')
