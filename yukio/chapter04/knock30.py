def read_mecab():
    i = 0
    sentences = []
    sentences.append([])
    for line in open("neko.txt.mecab", "r"):
        line = line.strip("\n")
        if line == "EOS":
            if sentences[i] != []:
                i += 1
                sentences.append([])
        else:
            line = line.replace("\t", ",")
            mecab = line.split(",")
            morpheme_dict = {}
            morpheme_dict["surface"] = mecab[0]
            morpheme_dict["base"] = mecab[7]
            morpheme_dict["pos"] = mecab[1]
            morpheme_dict["pos1"] = mecab[2]
            sentences[i].append(morpheme_dict)
    del sentences[-1]
    return sentences


if __name__ == "__main__":
    sentences = read_mecab()

    for line in sentences:
        print(line)
