from knock41 import get_cabocha
verb = []
mylist = []
for s in get_cabocha():
    for chunk in s:
        if any(m.pos == "動詞" for m in chunk.morphs):
            mylist = []
            for src in chunk.srcs:
                src_chunk = s[src]
                if any(m.pos == "助詞" for m in chunk.morphs):
                    line = [m.surface for m in chunk.morphs if m.pos == '助詞'][0]
                if line != "":
                    mylist.append(line)
        if len(mylist) != 0:
            if any(m.pos == "動詞" for m in chunk.morphs):
                mylist = set(mylist)
                join_line = ' '.join(mylist)
                print('{}\t{}'.format([m.base for m in chunk.morphs if m.pos == '動詞'][0], join_line))
