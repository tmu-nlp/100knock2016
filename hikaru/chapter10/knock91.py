import re

f = open("knock91.txt", "w")
switch = False
for line in open('word2vec/questions-words.txt'):
    if line.startswith(":"):
        if line == ': family\n':
            switch = True
        else:
            switch = False
    elif switch:
        f.write(line)
f.close()