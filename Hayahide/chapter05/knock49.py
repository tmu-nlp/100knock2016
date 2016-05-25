#-*- coding: utf-8 -*-
from knock48_2 import Morph, Chunk, Caboching, merge, search_pass

neko_list = Caboching()

for line in neko_list:
    for i in range(len(line)):
        xpass = []
        ypass = []
        iflag = 0
        for imorph in line[i].morphs:
            if imorph.pos == "名詞":
                iflag = 1
                break
        if iflag == 0:
            continue
        
        for j in range(i + 1, len(line)):
            jflag = 0
            for jmorph in line[j].morphs:
                if jmorph.pos == "名詞":
                    jflag = 1
                    break
            if jflag == 0:
                continue

            xpass = search_pass(line, line)
            ypass = search_pass(line, line[j:])
            if xpass == None or ypass == None:
                continue
            
            print (xpass)
            print (ypass)
            print (set(xpass + ypass))
            print ("\n")
            merge_pass = list(sorted(set(xpass + ypass)))
            merge_pass.pop(0)
            if len(xpass) == len(merge_pass):
                print (merge_pass)
                #ans_list = []
                #for ans in merge_pass:
                #    ans_list.append(merge(line[ans]))
                #ans_list.pop(0)
                #print (" -> ".join(ans_list))

