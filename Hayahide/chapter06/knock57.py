from graphviz import Digraph
import re
graph = Digraph(format="jpg")
graph.attr("node", shape="circle")

start = re.compile('<dependencies type="collapsed-dependencies">')
end = re.compile("</dependencies>")
gov = re.compile('<governor idx="(?P<gov_id>\d+)">(?P<governor>.+)</governor>')
dep = re.compile('<dependent idx="(?P<dep_id>\d+)">(?P<dependence>.+)</dependent>')
sentence = re.compile("<sentence>(?P<sentence_id>\d+)</sentence>")

sentence_id = 0
N = 2
count = 0
flag = False
for line in open("nlp.txt.out", "r"):
    start_check = start.search(line)
    gov_check = gov.search(line)
    dep_check = dep.search(line)

    if start_check:
        flag = True
    elif flag == True and gov_check:
        governor_id = gov_check.group("gov_id")
        graph.node("{}_{}".format(count, governor_id), gov_check.group("governor"))
    elif flag == True and dep_check:
        dep_id = dep_check.group("dep_id")
        graph.node("{}_{}".format(count, dep_id), dep_check.group("dependence"))
        graph.edge("{}_{}".format(count, dep_id), "{}_{}".format(count, governor_id))
    elif flag == True and end.search(line):
        count += 1
        flag = False
        if count > N:
            break

graph.render("corenlp_tree")
