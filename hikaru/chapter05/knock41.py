#-*-coding: utf-8-*-

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst.strip('D')
        self.srcs = srcs
    def chunklist(self):
        return [self.morphs, self.dst, self.srcs]

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1
    def morphlist(self):
        return [self.surface, self.base, self.pos, self.pos1]
def get_chunk_sentences():
    sentences = list()
    sentence = list()
    chunk = []
    morph = list()
    for line in open('neko.txt.cabocha', 'r'):
        if line.startswith('EOS'):
            if len(chunk) != 0: #最後の分節に入ったら
                sentence.append(chunk) #文のなかに分節を
            chunk = list() #分節空に
            if len(sentence) != 0:
                sentences.append(sentence)
            sentence = list()
        elif line.startswith('*'):
            if len(chunk) != 0: #次の分節に入ったら
                sentence.append(chunk) #文のなかに分節を
                chunk = list() #分節空に
            chunk = Chunk([], line.split()[2], line.split()[1]).chunklist()
        elif line.startswith('EOS') == False and line.startswith('*') == False:
            line = line.replace('\t', ',')
            word = line.split(',')
            morph = Morph(word[0], word[7], word[1], word[2]).morphlist()
            #sentence.append(morph)
            chunk[0].append(morph)
            #print (chunk) #確認
    return sentences

if __name__ == "__main__":
    ans = list()
    sub = list()
    sentences = get_chunk_sentences()
    sentence = sentences[7]
    for chunk in sentence:
        print (chunk)
        print('/')
