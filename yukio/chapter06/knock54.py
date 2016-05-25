import re

pattern_word = re.compile("<word>(?P<word>.+)</word>")
pattern_lemma = re.compile("<lemma>(?P<lemma>.+)</lemma>")
pattern_POS = re.compile("<POS>(?P<POS>.+)</POS>")
s = []

for line in open("nlp.txt.xml", "r"):
    if len(s) == 0 and re.search(pattern_word, line):
        s.append(re.search(pattern_word, line).group("word"))
    elif len(s) == 1 and re.search(pattern_lemma, line):
        s.append(re.search(pattern_lemma, line).group("lemma"))
    elif len(s) == 2 and re.search(pattern_POS, line):
        s.append(re.search(pattern_POS, line).group("POS"))
        print("\t".join(s))
        s = []
        
    
