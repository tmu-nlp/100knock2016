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
          s1 = []
          s2 = []
          for morph in y.morphs:
            if morph.pos == "動詞":
              s1.append("{}\t".format(morph.base))
              break
          for z in y.srcs:
            if not x[int(z)].isPos("助詞"):
              continue
            if x[int(z)].morphs[-1].surface == "、":
              x[int(z)].morphs.pop()
            s1.append("{} ".format(x[int(z)].morphs[-1].surface))
            s2.append("{} ".format(x[int(z)].morph_str("surface")))
          if s2 != []:
            s1.append("\t")
            s1.extend(s2)
            print("".join(s1))

