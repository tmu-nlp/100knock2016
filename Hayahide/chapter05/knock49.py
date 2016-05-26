#-*- coding: utf-8 -*-
from knock48 import Morph, Chunk, Caboching, merge

def search_path(line, chunk_num, goal):
    ans_list = [chunk_num]
    while ans_list[-1] != goal:
        ans_list.append(line[ans_list[-1]].dst)
    return ans_list

neko_list = Caboching()

for line in neko_list:
    for i in range(len(line)):
        for imorph in line[i].morphs:
            if imorph.pos == "名詞":
                imorph.surface = "X"
                break
        if imorph.surface != "X":
            continue

        for j in range(i + 1, len(line)):
            Y_esc = ""
            for jmorph in line[j].morphs:
                if jmorph.pos == "名詞":
                    Y_esc = jmorph.surface
                    jmorph.surface = "Y"
                    break
            if len(Y_esc) == 0:
                continue
            
            xpath = search_path(line, i, -1)
            ypath = search_path(line, j, -1)
            if xpath == None or ypath == None or len(ypath) == 0:
                continue
            
            merge_path = list(sorted(set(xpath + ypath)))
            ans_list = []
            if len(xpath) == len(merge_path):
                for temp in search_path(line, i, ypath[0]):
                    ans_list.append(merge(line[temp]))
                ans_list.pop()
                ans_list.append(jmorph.surface)
                print (" -> ".join(ans_list))
            else:
                ans = ""
                for temp in list(sorted(set(xpath) - set(ypath))):
                    ans_list.append(merge(line[temp]))
                ans += " -> ".join(ans_list) + " | "
                ans_list = []
                for temp in list(sorted(set(ypath) - set(xpath))):
                    ans_list.append(merge(line[temp]))
                ans += " -> ".join(ans_list) + " | "
                ans_list = []
                for temp in list(sorted(set(xpath) & set(ypath))):
                    ans_list.append(merge(line[temp]))
                ans_list.pop()
                ans += " -> ".join(ans_list)
                print (ans)

            jmorph.surface = Y_esc
