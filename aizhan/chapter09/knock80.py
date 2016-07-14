import re

for line in open('enwiki-20150112-400-r100-10576.txt'):
    if line != '\n':
        line = re.sub(r'\. |\.\n|[,!?;:()[]|[\'"]', ' ', line).split()
        print(' '.join(line))
