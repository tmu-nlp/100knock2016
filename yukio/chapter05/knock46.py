from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()

    for sentence in sentences:
        for chunk in sentence:
            predicate = ""
            case_flames = []
            for morph in chunk.getMorphs():
                if morph.getPos() == "動詞":
                    predicate = morph.getBase()
                    for i in chunk.getSrcs():
                        case = sentence[i].getMorphs()[-1]
                        if case.getPos() == "助詞":
                            morphs = ""
                            for morph2 in sentence[i].getMorphs():
                                morphs += morph2.getSurface()
                            case_flames.append([case.getBase(), morphs])
                    if case_flames != []:
                        case_flames.sort()
                        cases = []
                        chunks = []
                        for s1, s2 in case_flames:
                            cases.append(s1)
                            chunks.append(s2)
                        print("{}\t{}\t{}".format(predicate, " ".join(cases), " ".join(chunks)))
                    break
