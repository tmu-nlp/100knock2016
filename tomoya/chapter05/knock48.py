#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:10]:
  for y in x:
    if y.isPos("名詞"):
      print(y.morph_str("surface"), end = " ")

      while(y.dst != "-1"):
        print("->", end = " ")
        print(x[int(y.dst)].morph_str("surface"), end = " ")
        y = x[int(y.dst)]
    print() 
