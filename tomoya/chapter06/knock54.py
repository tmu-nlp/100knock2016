import re


word = re.compile("<word>(?P<word>.*)</word>")
lemma = re.compile("<lemma>(?P<lemma>.*)</lemma>")
pos = re.compile("<POS>(?P<POS>.*)</POS>")
tag = list()
for line in open("nlp.txt.out"):
    search_word = word.search(line)
    search_lemma = lemma.search(line)
    search_pos = pos.search(line)
    if search_word:
        print(search_word.group("word"), end="\t")
    elif search_lemma:
        print(search_lemma.group("lemma"), end="\t")
    elif search_pos:
        print(search_pos.group("POS"))
