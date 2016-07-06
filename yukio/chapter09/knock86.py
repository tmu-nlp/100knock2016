import numpy as np

vec = {}
for line in open("word_vec_85.txt", "r"):
    token, vector = line.strip("\n").split("\t")
    vec[token] = np.array(vector)

print("vec[United_States]")
print(vec["United_States"])
