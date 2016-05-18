from knock30 import read_mecab

sentences = read_mecab()
noun_phrase = []

for line in sentences:
    for morpheme in line:
        if len(noun_phrase) == 0:
            if morpheme["pos"] == "名詞":
                noun_phrase.append(morpheme["surface"])
        elif len(noun_phrase) == 1:
            if morpheme["surface"] == "の":
                noun_phrase.append(morpheme["surface"])
            elif morpheme["pos"] == "名詞":
                noun_phrase = [morpheme["surface"]]
            else:
                noun_phrase = []
        elif len(noun_phrase) == 2:
            if morpheme["pos"] == "名詞":
                noun_phrase.append(morpheme["surface"])
                print("".join(noun_phrase))
                noun_phrase = [morpheme["surface"]]
            else:
                noun_phrase = []
