import re


word = re.compile("<word>(?P<word>.*)</word>")
person = re.compile("<NER>PERSON</NER>")
for line in open("nlp.txt.out"):
    search_word = word.search(line)
    search_person = person.search(line)
    if search_word:
        word_person = search_word.group("word")
    elif search_person:
        print(word_person)
