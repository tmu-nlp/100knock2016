#-*-coding: utf-8-*-

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def morphprint(self):
        print ('surface:{}, base:{}, pos:{}, pos1:{}'.format(self.surface, self.base, self.pos, self.pos1))

def get_sentences():
    sentences = list()
    sentence = list()
    for line in open('neko.txt.cabocha', 'r'):
        if line.startswith('EOS'):
            if len(sentence) != 0:
                sentences.append(sentence)
                sentence = list()
        elif line.startswith('EOS') == False and line.startswith('*') == False:
            line = line.replace('\t', ',')
            word = line.split(',')
            morph = dict()
            morph['surface'] = word[0]
            morph['base'] = word[7]
            morph['pos'] = word[1]
            morph['pos1'] = word[2]
            sentence.append(morph)
    return sentences
            #classList.append(Morph(word[0], word[7], word[1], word[2]))
        #print ('surface:{}, base:{}, pos:{}, pos1:{}'.format(self.surface, self.base, self.pos, self.pos1))

if __name__ == "__main__":
    sentences = get_sentences()
    sentence = sentences[2]
    for morph in sentence:
        Morph(morph['surface'], morph['base'], morph['pos'], morph['pos1']).morphprint()
