from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()
    for sentence in sentences:
        for chunk in sentence:
            if chunk.getDst() != -1:
                s1 = ""
                s2 = ""
                for morph1 in chunk.getMorphs():
                    if morph1.getPos() != "記号":
                        s1 += morph1.getSurface()
                for morph2 in sentence[chunk.getDst()].getMorphs():
                    if morph2.getPos() != "記号":
                        s2 += morph2.getSurface()
                print("{}\t{}".format(s1, s2))
