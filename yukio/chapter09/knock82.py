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
    f = open("token_context_82.txt", "w")
    for token, context in extract_contexts():
        f.write("{}\t{}\n".format(token, context))
    f.close()
