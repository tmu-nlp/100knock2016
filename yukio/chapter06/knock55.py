import re

pattern_word = re.compile("<word>(?P<word>.+)</word>")
pattern_NER = re.compile("<NER>(?P<NER>.+)</NER>")
s = ""

for line in open("nlp.txt.xml", "r"):
    if s == "" and re.search(pattern_word, line):
        s = re.search(pattern_word, line).group("word")
    elif s != "" and re.search(pattern_NER, line):
        if re.search(pattern_NER, line).group("NER") == "PERSON":
            print(s)
        s = ""
        
    
