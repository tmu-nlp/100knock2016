from knock41 import get_cabocha

dst = ""
for sentence in get_cabocha():
    for chunk in sentence:
        if chunk.dst != -1:
            src = "".join(m.surface for m in chunk.morphs)
            for m in chunk.morphs:
                if m.pos != "記号":
                    #dst = "".join(m.surface)
                    
                    dst = "".join(m.surface for m in sentence[chunk.dst].getMorphs() )
            if src == "" or dst == "":
                continue
            print('{}\t{}'.format(src, dst))
