import sys
import re
from knock40 import Morph
def getChunk(): 
  class Chunk:
    def __init__(self, morphs, dst, srcs):
      self.morphs = morphs
      self.dst = dst
      self.srcs = srcs
    def isPos(self, pos):
      for x in self.morphs:
        if x.pos == pos:
          return True
      return False
    def morph_str(self, morph):
      temp = ""
      for x in self.morphs:
        if (morph == "surface"):
          temp += x.surface
        elif (morph == "base"):
          temp += x.base
      return temp.strip("。").strip("、")
  morph_list = []
  chunks = []
  sentence = []
  morphs = []
  srcs = []
  dst = None
  for line in open("neko.txt.cabocha"):
    if line[0] != "*" and "EOS" not in line:
      words = re.split("\t|,", line)
      morph_obj = Morph(words[0], words[7], words[1], words[2])
      morphs.append(morph_obj)
      morph_list.append(morph_obj)
    else:
      if line[0] == "*":
        if dst != None:
          chunks.append(Chunk(morphs, dst, srcs))
          morphs = []
          srcs = []
          dst = None
        words = re.split("\s", line)
        dst = words[2][:-1]
        for i, c in enumerate(chunks[:int(words[1])]):
          if c.dst == words[1]:
            srcs.append(i)
      if morphs != []:
        chunks.append(Chunk(morphs, dst, srcs))
        morphs = []
        srcs = []
        dst = None
      if "EOS" in line:
        sentence.append(chunks)
        chunks = []
        i = 0
  return sentence

if __name__ == "__main__":
  sentence = getChunk()
  for x in sentence[7]:
    for y in x.morphs:
      print(y.surface, end = "")
    print(" {}".format(x.dst))


