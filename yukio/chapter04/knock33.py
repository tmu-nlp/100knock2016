from knock30 import read_mecab

sentences = read_mecab()
for line in sentences:
    for morpheme in line:
        if morpheme["pos"] == "名詞" and morpheme["pos1"] == "サ変接続":
            print(morpheme["surface"])
