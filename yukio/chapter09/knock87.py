import numpy as np
def cos_sim(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

if __name__ == "__main__":
    vec = {}
    for line in open("word_vec_85.txt", "r"):
        token, vector = line.strip("\n").split("\t")
        vec[token] = np.array(vector)

    print("cos_sim(vec[United_States], vec[U.S])")
    print(cos_sim(vec["United_States"], vec["U.S"]))
