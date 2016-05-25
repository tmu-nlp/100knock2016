#-*- coding: utf-8 -*-
from knock41 import Morph, Chunk, Caboching

def chunk_merge(chunk):
    merge = ""
    for morph in chunk.morphs:
        if morph.pos != "記号":
            merge += morph.surface
    return merge

neko_list = Caboching()

for line in neko_list:
    for chunk in line:
        ans1 = chunk_merge(chunk)
        if ans1 == "":
            continue

        if chunk.dst != -1:
            ans2 = chunk_merge(line[chunk.dst])
            print (ans1 + "\t" + ans2)

