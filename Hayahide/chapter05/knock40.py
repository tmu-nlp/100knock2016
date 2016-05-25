#-*- coding: utf-8 -*-
import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

neko_list = []
morph_line = []
for line in open("neko.txt.cabocha", "r"):
    if line == "EOS\n":
        neko_list.append(morph_line)
        morph_line = []
    elif re.match("\*", line) == None and line != "EOS\n":
        word = re.split(",|\t", line)
        morph_line.append(Morph(word[0], word[7], word[1], word[2]))

ans = ""
for line in neko_list[2]:
    ans += line.surface
print (ans)
