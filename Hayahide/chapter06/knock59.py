import re
from nltk import Tree

parse_cmpl = re.compile("<parse>(?P<parse>.*)</parse>")

for line in open("nlp.txt.out", "r"):
    parse_check = parse_cmpl.search(line)
    if parse_check:
        trees = Tree.fromstring(parse_check.group("parse"))
        for parses in trees.subtrees(filter = lambda x: x.label() == "NP"):
            print(parses)
