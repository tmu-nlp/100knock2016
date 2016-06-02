import re

word = ""
lemma = ""
pos = ""
for line in open("nlp.txt.out", "r"):
        words = re.findall("<word>(.*)</word>", line)
        lemmas = re.findall("<lemma>(.*)</lemma>", line)
        poses = re.findall("<POS>(.*)</POS>", line)
        if len(words) > 0:
            word = words[0]
        elif len(lemmas) > 0:
            lemma = lemmas[0]
        elif len(poses) > 0:
            pos = poses[0]
        
        if len(word) > 0 and len(lemma) > 0 and len(pos) > 0:
            print (word + "\t" + lemma + "\t" + pos)
            word = ""
            lemma = ""
            pos = ""
