from knock41 import get_cabocha
verb = []
for sentence in get_cabocha():
    for chunk in sentence:
        if any(m.pos == "動詞" for m in chunk.morphs):
            mylist = []
            for src_num in chunk.srcs:
                src_chunk = sentence[src_num]
                if any(m.pos == "助詞" for m in chunk.morphs):
                    line = [m.surface for m in chunk.morphs if m.pos == '助詞'][0]
                if line is not None:
                        mylist.append(line, "".join(m.surface for m in self.morphs))
            if len(mylist) != 0:
                if any(m.pos == "動詞" for m in chunk.morphs):
                    verb = [m.base for m in chunk.morphs if m.pos == '動詞'][0]
                join_line = ' '.join(sorted(set(mylist)))
                print('{}\t{}'.format(verb, join_line))
