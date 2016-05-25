from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.getDst() != -1:
                s1 = ""
                s2 = ""
                noun_phrase_check = 0
                verb_phrase_check = 0
                for morph1 in chunk.getMorphs():
                    if morph1.getPos() != "記号":
                        s1 += morph1.getSurface()
                    if morph1.getPos() == "名詞":
                        noun_phrase_check = 1
                for morph2 in sentence[chunk.getDst()].getMorphs():
                    if morph2.getPos() != "記号":
                        s2 += morph2.getSurface()
                    if morph2.getPos() == "動詞":
                        verb_phrase_check = 1
                if noun_phrase_check and verb_phrase_check:
                    print("{}\t{}".format(s1, s2))
