import pickle

with open("word_vec_85.pickle", "rb") as f:
    vec = pickle.load(f)

print("vec[United_States]")
print(vec["United_States"])
