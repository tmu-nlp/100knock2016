from knock41 import get_cabocha
case_list = []
for s in get_cabocha():
    for chunk in s:
        if any(m.pos == "動詞" for m in chunk.morphs):
            case_list = []
            for src in chunk.srcs:
                src_chunk = s[src]
                if any(m.pos == "助詞" for m in chunk.morphs):
                    temp_case_list = [m.surface for m in chunk.morphs if m.pos == '助詞']
                    case_list += temp_case_list
            case_list = set(case_list)
            cases = ' '.join(case_list)

            if cases != "":
                pred = [m.base for m in chunk.morphs if m.pos == '動詞'][0]
                print('{}\t{}'.format(pred, cases))
