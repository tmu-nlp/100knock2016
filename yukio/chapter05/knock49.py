from knock40 import Morph
from knock41 import Chunk, read_cabocha

if __name__ == "__main__":
    sentences = read_cabocha()

    for sentence in sentences:
        for i, chunk1 in enumerate(sentence):
            s1 = ""
            noun_check1 = 0
            for morph1 in chunk1.getMorphs():
                if morph1.getPos() == "名詞":
                    s1 = "X"
                    noun_check1 = 1
                else:
                    s1 += morph1.getSurface()

            if noun_check1 == 1:
                for j, chunk2 in zip(range(i + 1, len(sentence)),sentence[i + 1:]):
                    s2 = "Y"
                    noun_check2 = 0
                    for morph2 in chunk2.getMorphs():
                        if morph2.getPos() == "名詞":
                            s2 += "Y"
                            s2 = s2.replace("YY", "Y")
                            noun_check2 = 1
                        else:
                            s2 += morph2.getSurface()
                    if noun_check2 == 1:
                        k = chunk1.getDst()
                        s3 = s1
                        s5 = ""
                        while k != -1 and k < j:
                            s3 += " -> "
                            for morph3 in sentence[k].getMorphs():
                                s3 += morph3.getSurface()
                            k = sentence[k].getDst()
                        if k == j:
                            print(s3 + " -> Y")

                        elif k != -1:
                            while k != -1:
                                l = chunk2.getDst()
                                s4 = s2

                                while l != -1 and l < k:
                                    s4 += " -> "
                                    for morph4 in sentence[l].getMorphs():
                                        s4 += morph4.getSurface()
                                    l = sentence[l].getDst()

                                if l == k:
                                    s5 = s3 + " | " + s4 + " | "
                                    for morph5 in sentence[l].getMorphs():
                                        s5 += morph5.getSurface()
                                    print(s5)
                                    break
                                else:
                                    s3 += " -> "
                                    for morph3 in sentence[k].getMorphs():
                                        s3 += morph3.getSurface()
                                    k = sentence[k].getDst()
