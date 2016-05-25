#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import re
from knock40 import Morph
from knock41 import getChunk

sentence = getChunk()
for x in sentence[:20]:
  for i in range(len(x)):
    if not x[i].isPos("名詞"):
      continue
    for j in range(i+1, len(x)):
      if not x[j].isPos("名詞"):
        continue
      pathI = set([i])
      pathJ = set([j])
      indexI = i
      indexJ = j
      while indexI != -1:
        indexI = int(x[indexI].dst)
        pathI.add(indexI)
      while indexJ != -1:
        indexJ = int(x[indexJ].dst)
        pathJ.add(indexJ)
      if j in pathI:
        path = list(sorted(pathI))
        path = path[1:path.index(j) + 1]
      else:
        temp = pathI.intersection(pathJ)
        pathI = sorted(list(pathI.difference(temp)))
        pathJ = sorted(list(pathJ.difference(temp)))
        path = sorted(list(temp))[1:]
        path.insert(0, pathI)
        path.insert(1, pathJ)

      for counter1, index in enumerate(path):
        if isinstance(index, int):
          if index == i:
            print("X{}".format(x[index].morphs[-1].surface), end = "")
          elif index == j:
            print("Y", end = "")
          else:
            x[index].print_chunk()
          if counter1 == len(path) - 1:
            print(end = " ")
          else:
            print(end = " -> ")

        elif isinstance(index, list):
          for counter2, index2 in enumerate(index):
            if index2 == i:
              print("X{}".format(x[index2].morphs[-1].surface), end = "")
            elif index2 == j:
              print("Y{}".format(x[index2].morphs[-1].surface), end = "")
            else:
              x[index2].print_chunk()
            if counter2 == len(index) - 1:
              print(end = " ")
            else:
              print(end = " -> ")
          print("|", end = " ")
      print()

