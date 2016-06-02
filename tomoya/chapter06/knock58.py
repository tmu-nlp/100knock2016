import re
from collections import defaultdict
search_type = re.compile('<dep type="(?P<dep_type>.*)">')
search_governor = re.compile('<governor idx="(?P<gov_idx>[0-9]*?)".*>(?P<governor>.*)</governor>')
search_dependent = re.compile('<dependent idx="(?P<dep_idx>[0-9]*?)".*>(?P<dependent>.*)</dependent>')
nsubj = defaultdict(list)
dobj = defaultdict(list)
flag = False

for line in open("nlp.txt.out"):
    if '<dependencies type="collapsed-dependencies">' in line:
        flag = True
    elif flag and "</dependencies>" in line:
        for predicate in set(nsubj.keys()) & set(dobj.keys()):
            prd1 = predicate.split(",")[1].strip()
            print("".join(nsubj[predicate]).split(",")[1].strip(), end="\t")
            print(predicate.split(",")[1].strip(), end="\t")
            print("".join(dobj[predicate]).split(",")[1].strip())
        nsubj = defaultdict(list)
        flag = False
    if flag:
        deptype = search_type.search(line)
        governor = search_governor.search(line)
        dependent = search_dependent.search(line)
        if deptype:
            dtype = deptype.group("dep_type")
        elif governor:
            gov = governor.group("gov_idx") + ", " + governor.group("governor")
        elif dependent:
            dep = dependent.group("dep_idx") + ", " + dependent.group("dependent")
            if dtype.strip() == "nsubj":
                nsubj[gov].append(dep)
            elif dtype.strip() == "dobj":
                dobj[gov].append(dep)
