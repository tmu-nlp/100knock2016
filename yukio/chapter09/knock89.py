import numpy as np
from knock77 import cos_sim
    
if __name__ == "__main__":
    vec = {}
    for line in open("word_vec_85.txt", "r"):
        token, vector = line.strip("\n").split("\t")
        vec[token] = np.array(vector)
    
    calc_vector = vec["Spain"] - vec["Madrid"] + vec["Athens"]
    sim_dic = {}
    for token, vector in sorted(vec.items()):
        sim_dic[token] = cos_sim(calc_vector, vector)

    for token, sim in sorted(sim_dic.items(), key = lambda x: x[1], reverse = True):
        print("{}\t{}".format(token, sim))
