import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence:
  for y in x:
    if y.dst != "-1":
      if y.isPos("名詞") and x[int(y.dst)].isPos("動詞"):
        y.print_chunk()
        print("\t", end = "")
        x[int(y.dst)].print_chunk()
        print("")        

