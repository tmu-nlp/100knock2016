#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:]:
  for y in x:
    s = []
    if y.isPos("動詞") and y.srcs != []: 
      print(y.morphs[0].base, end = "\t")
      for z in y.srcs:
        if x[int(z)].morphs[-1].surface == "、":
         x[int(z)].morphs.pop()
        s.append("{} ".format(x[int(z)].morphs[-1].surface))
      print("".join(sorted(set(s))))

