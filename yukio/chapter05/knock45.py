from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()
    f = open("verb_case_pattern.txt", "w")

    for sentence in sentences:
        for chunk in sentence:
            predicate = ""
            cases = []
            for morph in chunk.getMorphs():
                if morph.getPos() == "動詞":
                    predicate = morph.getBase()
                    for i in chunk.getSrcs():
                        case = sentence[i].getMorphs()[-1]
                        if case.getPos() == "助詞":
                            cases.append(case.getBase())
                    if cases != []:
                        f.write("{}\t{}\n".format(predicate, " ".join(sorted(cases))))
                    break
    f.close()

#cat verb_case_pattern.txt | sort | uniq -c | sort -r
#grep -e"^する\t" -e"^見る\t" -e"^与える\t" verb_case_pattern.txt | sort | uniq -c | sort -r
