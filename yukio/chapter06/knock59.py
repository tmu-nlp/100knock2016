import re
from nltk.tree import Tree

pattern_parse = re.compile("<parse>(?P<parse>.+)</parse>")

for line in open("nlp.txt.xml", "r"):
    if re.search(pattern_parse, line):
        tree = Tree.fromstring(re.search(pattern_parse, line).group("parse"))
        for subtree in tree.subtrees():
            if subtree.label() == "NP":
                print(" ".join(subtree.leaves()))
