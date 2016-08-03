human_list = list()
sim_list = list()

import numpy as np
def spearman(array_a, array_b):
    N = len(array_a)
    return 1 - (6 * sum(array_a - array_b) ** 2) / float(N**3 - N)

for line in open("knock94.txt"):
    word1, word2, human, sim = line.strip('\n').split(" ")
    human_list.append(float(human))
    sim_list.append(float(sim))

spe = spearman(np.array(sorted(human_list)), np.array(sorted(sim_list)))
print (spe)