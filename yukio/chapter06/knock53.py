import re

pattern_word = re.compile("<word>(?P<word>.+)</word>")
    
for line in open("nlp.txt.xml", "r"):
    if re.search(pattern_word, line):
        print(re.search(pattern_word, line).group("word"))
        
    
