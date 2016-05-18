from knock30 import read_mecab

sentences = read_mecab()
noun_phrase = []

for line in sentences:
    for morpheme in line:
        if morpheme["pos"] == "名詞":
            noun_phrase.append(morpheme["surface"])
        else:
            if len(noun_phrase) > 1:
                print("".join(noun_phrase))
            noun_phrase = []

if len(noun_phrase) > 1:
    print("".join(noun_phrase))
