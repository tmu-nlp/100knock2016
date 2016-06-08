import re

word = ""
lemma = ""
pos = ""
for line in open("nlp.txt.out", "r"):
    words = re.findall("<word>(.*)</word>", line)
    if len(words) > 0:
        word = words[0]
    if re.search("<NER>PERSON</NER>", line):
        print (word)
