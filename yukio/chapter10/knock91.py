import re

fout = open("data_91.txt", "w")
pattern = re.compile(": (?P<section>.+)")
family = False

for line in open("questions-words.txt", "r"):
    if pattern.search(line):
        if pattern.search(line).group("section") == "family":
            family = True
        else:
            family = False
    elif family:
        fout.write(line)

fout.close()
