from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()
    f = open("function_verb_case_flame.txt", "w")

    for sentence in sentences:
        for chunk in sentence:
            predicate1 = ""
            predicate2 = ""
            case_flames = []
            for morph in chunk.getMorphs():
                if morph.getPos() == "動詞":
                    predicate2 = morph.getBase()
                    for i in chunk.getSrcs():
                        case = sentence[i].getMorphs()[-1]
                        if case.getPos() == "助詞":
                            morphs = ""
                            for morph2 in sentence[i].getMorphs():
                                morphs += morph2.getSurface()
                            if case.getSurface() == "を" and sentence[i].getMorphs()[-2].getPos() == "名詞" and sentence[i].getMorphs()[-2].getPos1() == "サ変接続":
                                predicate1 = sentence[i].getMorphs()[-2].getSurface() + case.getSurface()
                            else:
                                case_flames.append([case.getBase(), morphs])
                    if predicate1 != "":
                        case_flames.sort()
                        cases = []
                        chunks = []
                        for s1, s2 in case_flames: 
                            cases.append(s1)
                            chunks.append(s2)
                        f.write("{}\t{}\t{}\n".format(predicate1 + predicate2, " ".join(cases), " ".join(chunks)))
                    break
    f.close()

#cut -f1 function_verb_case_flame.txt | sort | uniq -c | sort -r
#cut -f1,2 function_verb_case_flame.txt | sort | uniq -c | sort -r
