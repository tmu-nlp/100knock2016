from knock30 import read_mecab

sentences = read_mecab()
for line in sentences:
    for morpheme in line:
        if morpheme["pos"] == "動詞":
            print(morpheme["base"])
