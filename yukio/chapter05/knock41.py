from knock40 import Morph

class Chunk:
    def __init__(self, dst, srcs):
        self.morphs = []
        self.dst = dst
        self.srcs = srcs
    def appendMorphs(self, morph):
        self.morphs.append(morph)
    def getMorphs(self):
        return self.morphs
    def getDst(self):
        return self.dst
    def getSrcs(self):
        return self.srcs

def read_cabocha():
    i = 0
    j = 0
    sentences = []
    sentences.append([])
    for line in open("neko.txt.cabocha", "r"):
        line = line.strip("\n")
        if line == "EOS":
                i += 1
                j = 0
                sentences.append([])
        elif line[0] == "*":
            chunk = line.split()
            j = int(chunk[1])
            dst = int(chunk[2].strip("D"))
            srcs = []
            for k in range(0, j):
                if sentences[i][k].getDst() == j:
                    srcs.append(k)
            sentences[i].append(Chunk(dst, srcs))
        else:
            line = line.replace("\t", ",")
            cabocha = line.split(",")
            surface = cabocha[0]
            base = cabocha[7]
            pos = cabocha[1]
            pos1 = cabocha[2]
            sentences[i][j].appendMorphs(Morph(surface, base, pos, pos1))

    del sentences[-1]
    return sentences

if __name__ == "__main__":
    ans = []
    sentences = read_cabocha()
    for index, chunk in zip(range(0, len(sentences[7])), sentences[7]):
        s = ""
        for morph in chunk.getMorphs():
            s += morph.getSurface()
        print("{} {}\t--> {}".format(index, s, chunk.getDst()))
