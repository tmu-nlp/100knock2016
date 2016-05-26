import sys
import re
class Morph:
  def __init__(self, surface, base, pos, pos1):
    self.surface = surface
    self.base = base
    self.pos = pos
    self.pos1 = pos1
  def print_morph(self):
    print("surface:{}, base:{}, pos:{}, pos1:{}".format(self.surface, self.base, self.pos, self.pos1)) 
  def print_surface(self):
    print(self.surface)

def getMorph():
  morphs = []
  count = 0
  for line in open("neko.txt.cabocha"):
    if(line[0] != "*" and "EOS" not in line):
      words = re.split("\t|,", line)
      morph_obj = Morph(words[0], words[7], words[1], words[2])
      morphs.append(morph_obj)
      if count == 2:
        morph_obj.print_morph()
    elif "EOS" in line:
        count += 1


if __name__ == "__main__":
  getMorph()
