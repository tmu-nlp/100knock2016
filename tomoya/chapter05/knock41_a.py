# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import problem40


class Chunk():
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def __repr__(self):
        if self.morphs:
            surfs = [morph.surface for morph in self.morphs if morph.pos != '記号']
            return "".join(surfs)

    def include_pos(self, pos):
        return pos in [morph.pos for morph in self.morphs]

    def morphs_of_pos(self, pos):
        return [morph for morph in self.morphs if morph.pos == pos]

    def morphs_of_pos1(self, pos1):
        return [morph for morph in self.morphs if morph.pos1 == pos1]


def read_chunk(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line == "EOS\n":
            for idx, c in enumerate(sentence[:-1]):
                if c.dst != -1:
                    sentence[c.dst].srcs.append(idx)
            # if len(sentence) > 1:
                # sentences.append(sentence)
            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            chunk = Chunk()
            chunk.dst = int(line.split()[2].strip("D"))
            sentence.append(chunk)
        else:
            surface, other = line.split()
            others = other.split(",")
            base, pos, pos1 = others[6], others[0], others[1]
            morph = problem40.Morph(surface, base, pos, pos1)
            sentence[-1].morphs.append(morph)
    return sentences


if __name__ == "__main__":
    f = open("neko.txt.cabocha", "r")
    sentences = read_chunk(f)
    for idx, chnk in enumerate(sentences[7]):
        surfaces = ""
        for mrph in chnk.morphs:
            surfaces += mrph.surface
        print("%d" % idx, surfaces, "=>", chnk.dst)
    f.close()
