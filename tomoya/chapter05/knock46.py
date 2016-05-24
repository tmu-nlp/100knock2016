#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:]:
  for y in x:
        if y.isPos("動詞") and y.srcs != []:
          print(y.morphs[0].base, end = "\t")
          for z in y.srcs:
            if len(x[int(z)].morphs) < 1:
              continue
            print(x[int(z)].morphs[-1].base, end = " ")
          print("\t", end  = "")
          for z in y.srcs:
            print(x[int(z)].morph_str("surface"), end = " ")
          print("")
