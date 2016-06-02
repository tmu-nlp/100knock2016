import re

for line in open("nlp.txt.out", "r"):
    word = re.findall("<word>(.*)</word>", line)
    if len(word) > 0:
        print ("".join(word))
