import re
from graphviz import Digraph

pattern_start = re.compile('<dependencies type="collapsed-dependencies">')
pattern_end = re.compile('</dependencies>')
pattern_governor = re.compile('<governor idx="(?P<governor_id>[0-9]+)">(?P<governor>.+)</governor>')
pattern_dependent = re.compile('<dependent idx="(?P<dependent_id>[0-9]+)">(?P<dependent>.+)</dependent>')
pattern_sentence = re.compile('<sentence id="(?P<sentence_id>[0-9]+)">')
s = []
graph = Digraph(format = "png")
cd_check = 0
i = 0

for line in open("nlp.txt.xml", "r"):
    if re.search(pattern_start, line):
        cd_check = 1
    elif re.search(pattern_end, line):
        cd_check = 0

    elif cd_check == 1:
        if len(s) == 0 and re.search(pattern_governor, line):
            s.append([re.search(pattern_governor, line).group("governor_id"), re.search(pattern_governor, line).group("governor")])
        elif len(s) == 1 and re.search(pattern_dependent, line):
            s.append([re.search(pattern_dependent, line).group("dependent_id"), re.search(pattern_dependent, line).group("dependent")])
            graph.edge("{}.{}\n{}".format(i, s[0][0], s[0][1]), "{}.{}\n{}".format(i, s[1][0], s[1][1]))
            s = []

    elif re.search(pattern_sentence, line):
        i = int(re.search(pattern_sentence, line).group("sentence_id"))
    
    if i > 2:
        break

graph.render("tree")
