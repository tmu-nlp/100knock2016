import re
from collections import defaultdict


class Morph:

    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return 'surface:{}, base: {}, pos: {}, pos1: {}'.format(
            self.surface, self.base, self.pos, self.pos1)


class Chunk:
    def __init__(self, id, morphs, dst, srcs):
        self.id = id
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def __str__(self):
        return 'id: {}, dst: {}, srcs: {}'.format(str(self.id), str(self.dst), ','.join(str(i) for i in self.srcs))

    def join_surface(self):
        return ''.join(m.surface for m in self.morphs)

    def join_surface_wo_symbol(self):
        return ''.join(m.surface for m in self.morphs if m.pos != '記号')

    def in_noun(self):
        return any(m.pos == '名詞' for m in self.morphs)

    def in_verb(self):
        return any(m.pos == '動詞' for m in self.morphs)


def get_sentences():
    re_chunk = re.compile('\* (?P<id>[0-9]+?) (?P<dst>[0-9]+?)D .*')
    re_chunk_no_dst = re.compile('\* (?P<id>[0-9]+?) (?P<dst>-[0-9]+?)D .*')
    sentence = list()
    id2srcs = defaultdict(list)
    for line in open('neko.txt.cabocha'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                yield sentence
                id2srcs = defaultdict(list)
                sentence = list()
        elif line.startswith('*'):
            match = re_chunk.match(line)
            if match is None:
                match = re_chunk_no_dst.match(line)
            id = int(match.group('id'))
            dst = int(match.group('dst'))
            if dst != -1:
                id2srcs[dst].append(id)
            chunk = Chunk(id, list(), dst, id2srcs[id])
            sentence.append(chunk)
        else:
            surface = line.split('\t')[0]
            pos = line.split('\t')[1].split(',')[0]
            pos1 = line.split('\t')[1].split(',')[1].replace('*', '')
            base = line.split('\t')[1].split(',')[6]
            morph = Morph(surface, base, pos, pos1)
            chunk.morphs.append(morph)


if __name__ == '__main__':
    for i, sentence in enumerate(get_sentences()):
        if i == 7:
            for chunk in sentence:
                print(chunk)
                for morph in chunk.morphs:
                    print('\t', morph)
            break
