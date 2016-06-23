import random

def extract_contexts():
    result = []
    for line in open("tokens_81.txt", "r"):
        tokens = line.strip("\n").split()
        for i, token in enumerate(tokens):
            d = random.randint(1, 5)
            for j in range(i - d, i + d + 1):
                if j >= 0 and j < len(tokens) and i != j:
                    result.append([token, tokens[j]])
    return result

if __name__ == "__main__":
    for token, context in extract_contexts():
        print("{}\t{}".format(token, context))
