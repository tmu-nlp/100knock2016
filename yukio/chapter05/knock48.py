from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()

    for sentence in sentences:
        for chunk in sentence:
            s = ""
            noun_check = 0
            for morph in chunk.getMorphs():
                s += morph.getSurface()
                if morph.getPos() == "名詞":
                    noun_check = 1
            i = chunk.getDst()
            if noun_check == 1 and i != -1:
                while i != -1:
                    s += " -> "
                    for morph in sentence[i].getMorphs():
                        s += morph.getSurface()
                    i = sentence[i].getDst()
                print(s)
