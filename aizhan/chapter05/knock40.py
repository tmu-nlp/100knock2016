class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    
    def __str__(self):
        return 'surface:{}, base: {}, pos: {}, pos1: {}'.format(
                                                                self.surface, self.base, self.pos, self.pos1)


def get_sentences():
    sentence = list()
    for line in open('neko.txt.cabocha'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                yield sentence
                sentence = list()
            continue
        if line.startswith('*'):
            continue
        surface = line.split('\t')[0]
        pos = line.split('\t')[1].split(',')[0]
        pos1 = line.split('\t')[1].split(',')[1]
        base = line.split('\t')[1].split(',')[6]
        morph = Morph(surface, base, pos, pos1)
        sentence.append(morph)


for i, sentence in enumerate(get_sentences()):
    if i == 2:
        for morph in sentence:
            print(morph)
    break