import re

pattern_start = re.compile('<dependencies type="collapsed-dependencies">')
pattern_end = re.compile('</dependencies>')
pattern_dep_type = re.compile('<dep type="(?P<type>.+)">')
pattern_dep_end = re.compile('</dep>')
pattern_governor = re.compile('<governor idx="(?P<governor_id>[0-9]+)">(?P<governor>.+)</governor>')
pattern_dependent = re.compile('<dependent idx="(?P<dependent_id>[0-9]+)">(?P<dependent>.+)</dependent>')
pattern_sentence = re.compile('<sentence id="(?P<sentence_id>[0-9]+)">')

nsubjs = {}
dobjs = {}
cd_check = False
nsubj_check = False
dobj_check = False

for line in open("nlp.txt.xml", "r"):
    if re.search(pattern_start, line):
        cd_check = True
    elif re.search(pattern_end, line):
        cd_check = False
        for i in set(nsubjs.keys()) & set(dobjs.keys()):
            print("{}\t{}\t{}".format(nsubjs[i][1], nsubjs[i][0], dobjs[i][1]))
            
        nsubjs = {}
        dobjs = {}

    elif cd_check:
        if re.search(pattern_dep_type, line) and re.search(pattern_dep_type, line).group("type") == "nsubj":
            nsubj_check = True
        elif re.search(pattern_dep_type, line) and re.search(pattern_dep_type, line).group("type") == "dobj":
            dobj_check = True
        elif re.search(pattern_dep_end, line):
            nsubj_check = False
            dobj_check = False
        elif nsubj_check:
            if re.search(pattern_governor, line):
                governor_id = int(re.search(pattern_governor, line).group("governor_id"))
                nsubjs[governor_id] = [re.search(pattern_governor, line).group("governor")]
            elif re.search(pattern_dependent, line):
                nsubjs[governor_id].append(re.search(pattern_dependent, line).group("dependent"))
        elif dobj_check:
            if re.search(pattern_governor, line):
                governor_id = int(re.search(pattern_governor, line).group("governor_id"))
                dobjs[governor_id] = [re.search(pattern_governor, line).group("governor")]
            elif re.search(pattern_dependent, line):
                dobjs[governor_id].append(re.search(pattern_dependent, line).group("dependent"))
 
    
