#-*-coding: utf-8-*-

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = int(dst.strip('D'))
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
    chunk = Chunk([], '0', [])
    morph = Morph('0', '0', '0', '0')
    src_list = list()
    for line in open('neko.txt.cabocha', 'r'):
        if line.startswith('EOS'):
            if len(chunk.morphs) != 0: #最後の分節に入ったら
                sentence.append(chunk) #文のなかに分節を
                #print (type(chunk.morphs))
            chunk = Chunk([], '0', []) #分節空に
            if len(sentence) != 0:
                sentences.append(sentence)
            for src in src_list:
                if int(src[1]) != -1:
                    sentence[int(src[1])].srcs.append(int(src[0])) #chunkの2つめの[]に入ったはず
            sentence = list()
            src_list = list()
        elif line.startswith('*'):
            if len(chunk.morphs) != 0: #次の分節に入ったら
                sentence.append(chunk) #文のなかに分節を
                chunk = Chunk([], '0', []) #分節空に
            src_list.append([line.split()[1], line.split()[2].strip('D')])
            #chunk = Chunk([], line.split()[2], []).chunklist()
            chunk = Chunk([], line.split()[2], [])
        elif line.startswith('EOS') == False and line.startswith('*') == False:
            line = line.replace('\t', ',')
            word = line.split(',')
            #morph = Morph(word[0], word[7], word[1], word[2]).morphlist()
            morph = Morph(word[0], word[7], word[1], word[2])
            #sentence.append(morph)
            chunk.morphs.append(morph)
            #print (chunk) #確認
    return sentences


if __name__ == "__main__":
    sentences = get_chunk_sentences()
    p_list = list()
    pf_list = list()
    p_dic = {}
    x = {}
    #sentence = sentences[5]
    for sentence in sentences:
        chunk_list = list()
        sahenmorph_list = list()
        for chunk in sentence:
            chunk_list.append(chunk)
            for morph in chunk.morphs:
                if len(sahenmorph_list) == 1:
                    if morph.surface == 'を':
                        sahenmorph_list.append(morph.surface)
                        sahenmorph = ''.join(sahenmorph_list)
                    else:
                        sahenmorph_list = list()
                if morph.pos1 == 'サ変接続':
                    sahenmorph_list.append(morph.surface)

                if len(sahenmorph_list) == 2:
                    if morph.pos == '動詞':
                        v = sahenmorph + morph.base + '\t'
                        sahenmorph_list = list()
                        for src in chunk.srcs:
                            if chunk_list[src].morphs[-1].pos == '助詞' and chunk_list[src].morphs[-1].base != 'を':
                                p_f = ''
                                p_list.append(chunk_list[src].morphs[-1].base)
                                for morph2 in chunk_list[src].morphs:
                                    p_f += morph2.surface
                                pf_list.append(p_f)
                    if len(p_list) != 0:
                        for p, pf in zip(p_list, pf_list):
                            p_dic[p] = pf
                        keys, values = list(zip(*sorted(p_dic.items())))
                        #for key, value in sorted(p_dic.items()):
                            #x[key] = value
                        #ans = ' '.join(sorted(p_list)) + '\t' + ' '.join(sorted(pf_list, key=lambda x: x[::-1]))
                        #ans = ' '.join(p_dic.keys()) + '\t' + ' '.join(p_dic.values())
                        ans = ' '.join(keys) + '\t' + ' '.join(values)
                        p_list = list()
                        pf_list = list()
                        p_dic = {}
                        x = {}
                        print (v + ans)
                        break
