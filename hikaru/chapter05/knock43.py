#-*-coding: utf-8-*-

class Chunk:
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = int(dst.strip('D'))
        self.srcs = int(srcs)
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
    src = list()
    dst = list()
    morphs = str()
    nflag = False
    vflag = False
    nvflag = list()
    sentences = get_chunk_sentences()
    sentence = sentences[4]
    for chunks in sentence:
        dst.append(chunks[1]) #係り先インデックス番号抽出
        for chunk in chunks:
            if type(chunk) == list: #形態素解析部分の抽出
                for morph in chunk:
                    if morph[2] != '記号': #句読点は表示しない
                        if morph[2] == '名詞':
                            nflag = True
                        elif morph[2] == '動詞':
                            vflag = True
                        morphs += morph[0] #形態素をくっつけて分節に
                if nflag == True and vflag == False:
                    nvflag.append('np')
                elif nflag == False and vflag == True:
                    nvflag.append('vp')
                elif nflag == True and vflag == True:
                    nvflag.append('nvp')
                elif nflag == False and vflag == False:
                    nvflag.append('0')
                src.append(morphs) #係り元分節抽出 
                morphs = str()
                nflag = False
                vflag = False
        #print('/')
    #print (nvflag) #確認
    for i, j in enumerate(dst): #jが係り先番号 iが係り元番号
        if j != -1 and nvflag[i] == 'np' and nvflag[j] == 'vp':
            print (src[i] + '\t' + src[j])
        elif j != -1 and nvflag[i] == 'nvp' and nvflag[j] == 'vp':
            print (src[i] + '\t' + src[j])
        elif j != -1 and nvflag[i] == 'np' and nvflag[j] == 'nvp':    
            print (src[i] + '\t' + src[j])       
        elif j != -1 and nvflag[i] == 'nvp' and nvflag[j] == 'nvp':
            print (src[i] + '\t' + src[j])
        #elif j == -1:
        #    print (src[i])
