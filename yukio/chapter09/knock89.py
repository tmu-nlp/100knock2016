import numpy as np
from knock87 import cos_sim
import pickle

if __name__ == "__main__":
    with open("word_vec_85.pickle", "rb") as f:
        vec = pickle.load(f)
    
    calc_vector = vec["Spain"] - vec["Madrid"] + vec["Athens"]
    sim_dic = {}
    for token, vector in sorted(vec.items()):
        sim_dic[token] = cos_sim(calc_vector, vector)

    for (token, sim), i in zip(sorted(sim_dic.items(), key = lambda x: x[1], reverse = True), range(0, 1)):
        print("{}\t{}".format(token, sim))
