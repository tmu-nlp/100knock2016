import numpy as np

human = []
knock90 = []
human_dict = {}
knock90_dict = {}


def spearman(list_a, list_b):
    N = len(list_a)
    return 1 - ((6 * sum(map(lambda a, b: (a - b) ** 2, list_a, list_b))) / float(N ** 3 - N) )

for line in open("knock90_94.txt"):
    knock90 = line.strip().split("\t")
    knock90_dict["{} {}".format(knock90[0],knock90[1])] = float(knock90[2])

for l in open("combined.tab"):
    human = l.strip().split("\t")
    try:
        human_dict["{} {}".format(human[0],human[1])] = float(human[2])
    except:
        pass
rankh = []
rank90 = []
for a,b in zip(sorted(knock90_dict.items(), key=lambda x:x[1]), sorted(human_dict.items(), key=lambda x:x[1])):
    rankh.append(list(a).pop(1))
    rank90.append(list(b).pop(1))
print(rankh,rank90)
print(spearman(rankh,rank90))
