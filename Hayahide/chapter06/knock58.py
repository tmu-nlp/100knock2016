import re

start = re.compile('dependencies type="collapsed-dependencies">')
end = re.compile("</dependencies>")
types = re.compile('<dep type="(?P<dep_type>.+)">')
gov = re.compile('<governor idx="(?P<id>\d+)">(?P<governor>.+)</governor>')
dep = re.compile('<dependent idx="(?P<dep_id>\d+)">(?P<dependence>.+)</dependent>')

flag = False
nsubj = {}
dobj = {}
gov_dict = {}
type_name = ""
for line in open("nlp.txt.out", "r"):
    types_check = types.search(line)
    gov_check = gov.search(line)
    dep_check = dep.search(line)

    if start.search(line):
        flag = True

    if flag == False:
        continue

    if types_check:
        type_name = types_check.group("dep_type")
        if type_name != "nsubj" and type_name != "dobj":
            type_name = ""
    elif len(type_name) > 0 and gov_check:
        gov_dict[gov_check.group("id")] = gov_check.group("governor")
        gov_id = gov_check.group("id")
    elif len(type_name) > 0 and dep_check:
        if type_name == "nsubj":
            nsubj[gov_id] = dep_check.group("dependence")
        elif type_name == "dobj":
            dobj[gov_id] = dep_check.group("dependence")
        type_name = ""
    elif end.search(line):
        for key, value in gov_dict.items():
            if key in nsubj and key in dobj:
                print(nsubj[key] + "\t" + value + "\t" + dobj[key])
        nsubj = {}
        dobj = {}
        gov_dict = {}
        flag = False
