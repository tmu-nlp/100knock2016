import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence:
  for y in x:
    if y.dst != "-1":
      if y.isPos("名詞") and x[int(y.dst)].isPos("動詞"):
        print(y.morph_str("surface"), end = "")
        print("\t", end = "")
        print(x[int(y.dst)].morph_str("surface"))

