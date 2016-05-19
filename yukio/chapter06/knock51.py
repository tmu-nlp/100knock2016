from knock50 import sentence_punc

def word_punc():
    return sentence_punc().replace("\n", "\n\n").replace(" ", "\n")

if __name__ == "__main__":
    print(word_punc())
