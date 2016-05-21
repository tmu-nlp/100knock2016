#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:]:
  for y in x:
        if len(y.morphs) >= 2 and y.morphs[0].pos1 == "サ変接続" and y.morphs[1].base == "を":
          print("{}を{}".format(y.morphs[0].base, x[int(y.dst)].morphs[0].base), end = "\t")
          for z in x[int(y.dst)].srcs:
            print(x[int(z)].morphs[-1].base, end = " ")
          print("\t", end = "")

          for z in x[int(y.dst)].srcs:
            print(x[int(z)].morph_str("surface"), end = " ")
          print()

