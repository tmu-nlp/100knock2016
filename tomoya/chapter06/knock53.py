import re


word = re.compile("<word>(?P<word>.*)</word>")
for line in open("nlp.txt.out"):
    search_word = word.search(line)
    if search_word:
        print(search_word.group("word"))
