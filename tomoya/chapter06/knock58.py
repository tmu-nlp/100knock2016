import re
from collections import defaultdict
search_type = re.compile('<dep type="(.*)">')
search_governor = re.compile('<governor idx="([0-9]*?)".*>(.*)</governor>')
search_dependent = re.compile('<dependent idx="([0-9]*?)".*>(.*)</dependent>')
search_dependencies = re.compile('')
nsubj = defaultdict(list)
dobj = defaultdict(list)
flag = False

for line in open("nlp.txt.out"):
    if '<dependencies type="collapsed-dependencies">' in line:
        flag = True
    elif flag == True and "</dependencies>" in line:
        for predicate in  set(nsubj.keys()) & set(dobj.keys()):
            prd1 = predicate.split(",")[1].strip()
            print("".join(nsubj[predicate]).split(",")[1].strip(), end = "\t")
            print(predicate.split(",")[1].strip(), end = "\t") 
            print("".join(dobj[predicate]).split(",")[1].strip())
        #print(set(nsubj.keys()) & set(dobj.keys()))
        nsubj = defaultdict(list)
        flag = False
    if flag:
        deptype = search_type.search(line)
        governor = search_governor.search(line)
        dependent = search_dependent.search(line)
        if deptype:
            dtype = deptype.group(1)
        elif governor:
            gov = governor.group(1) + ", " +  governor.group(2)
        elif dependent:
            dep = dependent.group(1) + ", " + dependent.group(2)
            if dtype.strip() == "nsubj":
                nsubj[gov].append(dep)
            elif dtype.strip() == "dobj":
                dobj[gov].append(dep)

