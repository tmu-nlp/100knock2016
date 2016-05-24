#-*- coding: utf-8 -*-
from knock43 import Morph, Chunk, Caboching

neko_list = Caboching()

def merge(chunk):
    merge = ""
    for morph in chunk.morphs:
        if morph.pos != "記号":
            merge += morph.surface
    return merge

for line in neko_list:
    for chunk in line:
        verb = ""
        for morph in chunk.morphs:
            if morph.pos == "動詞":
                verb = morph.base
                break
        if verb == "":
            continue
        
        flag = 0
        particles = {}
        for src in chunk.srcs:
            morph = line[src].morphs
            if morph[-1].pos == "助詞":
                particles[morph[-1].base] = merge(line[src])
                flag = 1
        if flag == 1:
            particle_list = []
            particle_chunk = []
            for key, value in sorted(particles.items()):
                particle_list.append(key)
                particle_chunk.append(value)
            if "を" in particle_list:
                verb = str(particle_chunk[-1]) + verb
                print (verb + "\t" + " ".join(particle_list) + "\t" + " ".join(particle_chunk))
