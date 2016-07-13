f = open('knock80.txt', 'w')
for line in open('enwiki-20150112-400-r100-10576.txt'):
    words = line.strip("\n").split()
    l = list()
    for word in words:
        word = word.strip(".,!?;:()[]'")
        word = word.strip('"')
        if word != '':
            l.append(word)
    f.write(' '.join(l) + "\n")
f.close()
