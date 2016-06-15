f = open("tokens_80.txt", "w")

for line in open("enwiki-20150112-400-r100-10576.txt", "r"):
    tokens = line.strip("\n").split(" ")
    result = []
    for token in tokens:
        token = token.strip(".,!?;:()[]'\"")
        if token != "":
            result.append(token)
    f.write(" ".join(result) + "\n")

f.close()
