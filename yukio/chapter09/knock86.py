import pickle

def knock_86(vec):
    print("vec[United_States]")
    print(vec["United_States"])

if __name__ == "__main__":
    with open("word_vec_85.pickle", "rb") as f:
        vec = pickle.load(f)
    knock_86(vec)
