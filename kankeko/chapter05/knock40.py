import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def __str__(self):
        return 'surface:{}, base: {}, pos: {}, pos1: {}'.format(self.surface, self.base, self.pos, self.pos1)

def get_tag(line):
    surface = re.split(r'\t|,',line)[0]
    pos = re.split(r'\t|,',line)[1]
    pos1 = re.split(r'\t|,',line)[2]
    base = re.split(r'\t|,',line)[7]
    return Morph(surface, base, pos, pos1)

def neko_cabocha():
    s = []
    for line in open('neko.txt.cabocha'):
        line = line.strip()
        if line == 'EOS':
            if len(s) != 0:
                yield s
                s = []
            continue
        if line.startswith('*'):
            continue
        morph = get_tag(line)
        s.append(morph)

if __name__ == "__main__":
    for i,line in enumerate(neko_cabocha()):
        if i == 2:
            for morph in line:
                print(morph)
            break
