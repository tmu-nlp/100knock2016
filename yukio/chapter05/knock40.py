class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def getSurface(self):
        return self.surface
    def getBase(self):
        return self.base
    def getPos(self):
        return self.pos
    def getPos1(self):
        return self.pos1

def read_cabocha():
    i = 0
    sentences = []
    sentences.append([])
    for line in open("neko.txt.cabocha", "r"):
        line = line.strip("\n")
        if line == "EOS":
                i += 1
                sentences.append([])
        elif line[0] != "*":
            line = line.replace("\t", ",")
            cabocha = line.split(",")
            surface = cabocha[0]
            base = cabocha[7]
            pos = cabocha[1]
            pos1 = cabocha[2]
            sentences[i].append(Morph(surface, base, pos, pos1))

    del sentences[-1]
    return sentences

if __name__ == "__main__":
    ans = []
    sentences = read_cabocha()
    for morph in sentences[2]:
        ans.append(morph.getSurface())
    print(ans)
