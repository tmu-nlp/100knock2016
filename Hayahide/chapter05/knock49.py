#-*- coding: utf-8 -*-
from knock48_2 import Morph, Chunk, Caboching, merge

def search_pass(line, chunk_num, goal):
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
            
            xpass = search_pass(line, i, -1)
            ypass = search_pass(line, j, -1)
            if xpass == None or ypass == None or len(ypass) == 0:
                continue
            
            merge_pass = list(sorted(set(xpass + ypass)))
            ans_list = []
            if len(xpass) == len(merge_pass):
                for temp in search_pass(line, i, ypass[0]):
                    ans_list.append(merge(line[temp]))
                ans_list.pop()
                ans_list.append(jmorph.surface)
                print (" -> ".join(ans_list))
            else:
                ans = ""
                for temp in list(sorted(set(xpass) - set(ypass))):
                    ans_list.append(merge(line[temp]))
                ans += " -> ".join(ans_list) + " | "
                ans_list = []
                for temp in list(sorted(set(ypass) - set(xpass))):
                    ans_list.append(merge(line[temp]))
                ans += " -> ".join(ans_list) + " | "
                ans_list = []
                for temp in list(sorted(set(xpass) & set(ypass))):
                    ans_list.append(merge(line[temp]))
                ans_list.pop()
                ans += " -> ".join(ans_list)
                print (ans)

            jmorph.surface = Y_esc
