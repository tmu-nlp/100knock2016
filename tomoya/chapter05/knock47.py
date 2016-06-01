#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:]:
  for i, y in enumerate(x):
        if len(y.morphs) >= 2 and y.morphs[0].pos1 == "サ変接続" and y.morphs[1].base == "を":
          s1 = []
          s2 = []
          s1.append("{}を{}\t".format(y.morphs[0].base, x[int(y.dst)].morphs[0].base))
          for z in x[int(y.dst)].srcs:
            if z == i:
              continue
            if x[int(z)].morphs[-1].base == "、":
              x[int(z)].morphs.pop()
            if x[int(z)].isPos("助詞"):
              s1.append("{} ".format(x[int(z)].morphs[-1].surface))
              s2.append("{} ".format(x[int(z)].morph_str("surface")))
          s1.append("\t")
          s2.extend(s2)
          print("".join(s1))
