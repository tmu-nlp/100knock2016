import numpy as np
import pickle

def cos_sim(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def knock_87(vec):
    print("cos_sim(vec[United_States], vec[U.S])")
    print(cos_sim(vec["United_States"], vec["U.S"]))

if __name__ == "__main__":
    with open("word_vec_85.pickle", "rb") as f:
        vec = pickle.load(f)

    knock_87(vec)
