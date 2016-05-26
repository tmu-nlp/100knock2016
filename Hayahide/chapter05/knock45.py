#-*- coding: utf-8 -*-
from knock43 import Morph, Chunk, Caboching

neko_list = Caboching()

for line in neko_list:
    for chunk in line:
        verb = ""
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb = morph.base
        if verb == "":
            continue
        
        particles = []
        for src in chunk.srcs:
            morph = line[src].morphs
            if morph[-1].pos1 == "格助詞":
                particles.append(morph[-1].base)
        if particles != []:
            print (verb + "\t" + " ".join(sorted(particles)))
