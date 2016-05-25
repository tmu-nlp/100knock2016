#-*- coding: utf-8 -*-

class Morph:
    def __init__(self, line):
        line = line.replace("\t", ",")
        word = line.split(",")
        self.surface = word[0]
        self.base = word[7]
        self.pos = word[1]
        self.pos1 = word[2]

class Chunk:
    def __init__(self):
        self.srcs = []
        self.morphs = []

    def set_dst(self, line):
        word = line.split(" ")
        word[2]= int(word[2].replace("D", ""))
        self.dst = word[2]
        return [int(word[1]), word[2]]  #左は文節番号、右は係り先
    
    def append_list(self, lists, objects): #class内のリストにappend
        lists.append(objects)

def Caboching():
    neko_list = []
    chunk_list = []
    src_list = []
    for line in open("neko.txt.cabocha", "r"):
        if line == "EOS\n":
            for src in src_list:    #src_listの長さは文節の長さ
                if src[1] != -1:
                    chunk_list[src[1]].append_list(chunk_list[src[1]].srcs, src[0])
                #係り先のChunkクラス内の係り元リストに文節番号を追加
            neko_list.append(chunk_list)
            chunk_list = []
            src_list = []

        elif line.split()[0] == "*":     
            chunk_class = Chunk()   #Chunkクラスの作成
            src_list.append(chunk_class.set_dst(line))  #係り元と係り先を格納
            chunk_list.append(chunk_class)

        elif line != "EOS\n":
            chunk_list[-1].append_list(chunk_list[-1].morphs, Morph(line))

    return neko_list

if __name__ == "__main__":
    neko_list = Caboching()
    ans = ""
    for classes in neko_list[7]:
        for morph in classes.morphs:
            ans += morph.surface
       
