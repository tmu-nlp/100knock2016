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
    ans_list = list()
    st_chunk1 = ''
    st_chunk2 = ''
    st_chunk3 = ''
    for sentence in sentences:
        for i, chunk1 in enumerate(sentence):
            n1_flag = 0
            n2_flag = 0
            for morph in chunk1.morphs:
                if morph.pos == '名詞':
                    n1_flag = 1
                    st_chunk1 = ''.join(m.surface if m.pos != '名詞' else 'X' for m in chunk1.morphs)#内包表記でsurfaceだけを追加
                    st_chunk1 = st_chunk1.strip().strip('、').strip('。')
                    for j, chunk2 in zip(range(i+1, len(sentence[i+1:])), sentence):
                        n2_flag = 0
                        for morph2 in chunk2.morphs:
                            if morph2.pos == '名詞':
                                n2_flag = 1
                                st_chunk2 = ''.join(m.surface if m.pos != '名詞' else 'Y' for m in chunk2.morphs)  # 内包表記でsurfaceだけを追加
                                st_chunk2 = st_chunk2.strip().strip('、').strip('。')
                                chunk3 = chunk2
                                while chunk3.dst != chunk1.dst:
                                    #if chunk.dst != chunk2.dst:
                                    chunk3 = sentence[chunk2.dst]
                                    #for morph2 in chunk2.morphs:
                                    st_chunk3 += ''.join(m.surface for m in chunk3.morphs)
                                        #st_chunk2 += morph2.surface
                                    st_chunk3 = st_chunk3.strip('。').strip('、')
                                    st_chunk3 += '->'
                                    n2_flag = 1
                    if n2_flag == 1:
                        st_chunk3 = st_chunk3.strip('->').strip('。').strip('、')
                        st_chunk2 = st_chunk2 + '\t' + st_chunk3
            if n1_flag == 1:
                st_chunk2 = st_chunk2.strip('->').strip('。').strip('、')
                print (st_chunk + '\t' + st_chunk2 + '\t' + st_chunk3)
            st_chunk3 = ''
            st_chunk2 = ''
            st_chunk1 = ''
