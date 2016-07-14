from knock87 import cos_sim
import pickle

def knock_88(vec):
    sim_dic = {}
    for token, vector in sorted(vec.items()):
        if token != "England":
            sim_dic[token] = cos_sim(vec["England"], vector)

    for (token, sim), i in zip(sorted(sim_dic.items(), key = lambda x: x[1], reverse = True), range(0, 10)):
        print("{}\t{}".format(token, sim))

if __name__ == "__main__":
    with open("word_vec_85.pickle", "rb") as f:
        vec = pickle.load(f)
    
    knock_88(vec)
