import re
from nltk.tree import Tree
search_parse = re.compile("<parse>\(ROOT (.*)\) </parse>")

for line in open("nlp.txt.out"):
    parse = search_parse.search(line)
    if parse:
        t = Tree.fromstring(parse.group(1))
        for i in t.subtrees(filter=lambda x: x.label() == 'NP'):
            print(i)
