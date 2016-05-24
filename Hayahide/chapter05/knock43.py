#-*- coding: utf-8 -*-
from knock41 import Morph, Chunk, Caboching

def chunk_merge(chunk, cpos):
    flag = 0
    merge = ""
    for morph in chunk.morphs:
        if morph.pos != "記号":
            merge += morph.surface
        if morph.pos == cpos:
            flag = 1
    
    return merge if flag == 1 else ""

if __name__ == "__main__":
    neko_list = Caboching()

    for line in neko_list:
        for chunk in line:
            ans1 = chunk_merge(chunk, "名詞")
            if ans1 == "":
                continue

            if chunk.dst != -1:
                ans2 = chunk_merge(line[chunk.dst], "動詞")
            else:
                ans2 = ""

            if ans2 != "":
                print (ans1 + "\t" + ans2)
