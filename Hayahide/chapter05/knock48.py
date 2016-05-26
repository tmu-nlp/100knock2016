#-*- coding: utf-8 -*-
from knock41 import Morph, Chunk, Caboching

def merge(chunk):
    merge = ""
    for morph in chunk.morphs:
        if morph.pos != "記号":
            merge += morph.surface
    return merge

def search_pass(line):
    for chunk in line:
        ans_list = []
        for morph in chunk.morphs:
            if morph.pos == "名詞":
                ans_list.append(merge(chunk))
                break
        if len(ans_list) == 0 or chunk.dst == -1:
            continue

        temp_dst = chunk.dst
        while temp_dst != -1:
            ans_list.append(merge(line[temp_dst]))
            temp_dst = line[temp_dst].dst
        return ans_list

if __name__ == "__main__":
    neko_list = Caboching()
    for line in neko_list:
        ans_list = search_pass(line)
        if ans_list != None:
            print (" -> ".join(ans_list))
