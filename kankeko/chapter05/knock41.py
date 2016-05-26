import re
from collections import defaultdict
from knock40 import Morph,get_tag

class Chunk:
    def __init__(self, id, morphs, dst, srcs):
        self.id = id
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    def getMorphs(self):
        return self.morphs
    
    def __str__(self):
        return 'id: {}, dst: {}, srcs: {}'.format(str(self.id), str(self.dst), ','.join(str(i) for i in self.srcs))
    
    def join_surface(self):
        return ''.join(m.surface for m in self.morphs)

    def join_surface_wo_symbol(self):
            return ''.join(m.surface for m in self.morphs if m.pos != '記号')
    
    def has_noun(self):
        return any(m.pos == '名詞' for m in self.morphs)
    
    def has_verb(self):
        return any(m.pos == '動詞' for m in self.morphs)
    
    def has_particle(self):
        return any(m.pos == '助詞' for m in self.morphs)
    
    def get_most_left_verb(self, form=lambda m: m.base):
        if self.has_verb():
            return [form(m) for m in self.morphs if m.pos == '動詞'][0]

    def get_most_right_particle(self):
        if self.has_particle():
            return [m.surface for m in self.morphs if m.pos == '助詞'][0]

    def is_sahen_wo(self):
        return len(self.morphs) >= 2 and self.morphs[0].pos1 == 'サ変接続' and self.morphs[1].surface == 'を'

    def get_path_to_root(self, sentence, form=lambda ch: ch.join_surface_wo_symbol()):
        path = [form(self)]
        dst = self.dst
        while dst != -1:
            next_chunk = sentence[dst]
            path.append(form(next_chunk))
            dst = next_chunk.dst
        return path

    def get_path_to_id(self, sentence, target_id, form=lambda ch: ch.join_surface_wo_symbol(), include_id=True):
        path = [form(self)]
        dst = self.dst
        current = self.id
        while current != target_id:
            next_chunk = sentence[dst]
            path.append(form(next_chunk))
            dst = next_chunk.dst
            current = next_chunk.id
        if not include_id:
            path.pop(-1)
        return path

    def replace_noun(self, name):
        return ''.join(m.surface if m.pos != '名詞' else name for m in self.morphs if m.pos != '記号')



def get_cabocha():
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
            morph = get_tag(line)
            chunk.morphs.append(morph)


if __name__ == '__main__':
    for i, sentence in enumerate(get_cabocha()):
        if i == 7:
            for chunk in sentence:
                print(chunk)
                for morph in chunk.morphs:
                    print('\t', morph)
            break


