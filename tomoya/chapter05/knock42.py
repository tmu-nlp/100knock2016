import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence:
  for y in x:
    if y.dst != "-1":
      y.print_chunk()
      print(" ", end = "")
      x[int(y.dst)].print_chunk()
      print() 
